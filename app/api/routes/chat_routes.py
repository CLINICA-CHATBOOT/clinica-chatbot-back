# -*- coding: utf-8 -*-
from fastapi import APIRouter, HTTPException
from app.models.chat import Message, ResponseMessage, Appointment
from app.services.responder import get_gemini_reply
from app.db.database import get_conexion
from app.db.models import tabla_professionals, tabla_appointments
from datetime import datetime

router = APIRouter()

TURNOS_TEMP = {}

DIRECTORIO = {
    "Cardiología": ["Dr. Juan Rodríguez", "Dra. Marta Pérez"],
    "Dermatología": ["Dr. Pedro Gómez", "Dra. Ana López"],
    "Neurología": ["Dr. Luis Fernández", "Dra. María Torres"],
    "Pediatría": ["Dr. Pablo Díaz", "Dra. Laura Sánchez"],
}

@router.get("/")
def index():
    return {"message": "Bienvenido al Chatbot de la Clínica"}

@router.post("/chat/respond", response_model=ResponseMessage)
def chat_mensaje(message: Message):
    user_message = message.content.lower()

    # Listar especialidades
    if "especialidad" in user_message or "especialidades" in user_message:
        lista = "\n - " + "\n - ".join(DIRECTORIO.keys())
        return {"response": f"Las especialidades disponibles son:\n{lista}"}
    
    # Listar profesionales
    if any(palabra in user_message for palabra in ["profesional", "profesionales", "doctor", "doctores"]):
        respuesta = []
        for especialidad, profesionales in DIRECTORIO.items():
            lista = f"{especialidad}:\n - " + "\n - ".join(profesionales)
            respuesta.append(lista)
        return {"response": "Profesionales disponibles:\n\n" + "\n\n".join(respuesta)}
    
    # Listar profesionales por especialidad
    for especialidad, profesionales in DIRECTORIO.items():
        if especialidad.lower() in user_message:
            lista = "\n - " + "\n - ".join(profesionales)
            return {"response": f"Los profesionales en {especialidad} son:\n{lista}"}
        
    # Agendar turno
    if any(palabra in user_message for palabra in ["sacar un turno", "quiero un turno", "cita", "agendar", "reservar"]):
        TURNOS_TEMP["step"] = "ask_professional"
        return {"response": "Perfecto. ¿Con qué profesional deseas el turno?"}

    # Guardar profesional
    if TURNOS_TEMP.get("step") == "ask_professional":
        TURNOS_TEMP["professional_name"] = message.content
        TURNOS_TEMP["step"] = "ask_name"
        return {"response": "Anotado. ¿Cuál es el nombre del paciente?"}

    # Guardar nombre del paciente
    if TURNOS_TEMP.get("step") == "ask_name":
        TURNOS_TEMP["patient_name"] = message.content
        TURNOS_TEMP["step"] = "ask_date"
        return {"response": "Gracias. ¿Qué fecha y horario deseas para el turno? (ej: 15/11/2025 10:30)"}
    
    # Guardar fecha y crear turno
    if TURNOS_TEMP.get("step") == "ask_date":
        raw_date = message.content.strip()

        try:
            # el usuario manda "15/11/2025 10:30"
            dt = datetime.strptime(raw_date, "%d/%m/%Y %H:%M")

            # guardar en formato para la BD
            db_date = dt.strftime("%Y-%m-%d %H:%M")

            # mostrar al usuario en formato original
            display_date = dt.strftime("%d/%m/%Y %H:%M")

            TURNOS_TEMP["appointment_date_db"] = db_date
            TURNOS_TEMP["appointment_date_display"] = display_date

        except ValueError:
            return {"response": "Formato inválido. Usa el formato DD/MM/YYYY HH:MM (ej: 15/11/2025 10:30)"}

        # Buscar el ID del profesional en la BD
        conexion = get_conexion()
        cursor = conexion.execute(
            "SELECT id FROM professionals WHERE name = ?", (TURNOS_TEMP["professional_name"],)
        )
        profesional = cursor.fetchone()
        conexion.close()

        if not profesional:
            TURNOS_TEMP.clear()
            return {"response": "No encontré ese profesional. Intenta de nuevo."}

        # Construir el objeto Appointment y llamar a crear_turno_medico
        appointment = Appointment(
            professional_id=profesional["id"],
            patient_name=TURNOS_TEMP["patient_name"],
            appointment_date=TURNOS_TEMP["appointment_date_db"]
        )
        turno = crear_turno_medico(appointment)

        datos = TURNOS_TEMP.copy()
        TURNOS_TEMP.clear()
        return {
            "response": f"{turno['message']}\n\n"
                        f"Profesional: {datos['professional_name']}\n"
                        f"Paciente: {datos['patient_name']}\n"
                        f"Fecha: {datos['appointment_date_display']}"
        }

    # Respuesta por defecto usando Gemini
    response = get_gemini_reply(message.content)
    return {"response": response}


@router.get("/directory/specialties")
def listar_especialidades():
    return {"specialties": list(DIRECTORIO.keys())}

@router.get("/directory/professionals/{specialty}")
def listar_profesionales(specialty: str):
    profesionales = DIRECTORIO.get(specialty, [])
    return {"specialty": specialty, "professionals": profesionales}

@router.post("/appointments")
def crear_turno_medico(appointment: Appointment):
    tabla_appointments()

    conexion = get_conexion()

    # validar que el profesional existe
    cursor = conexion.execute(
        "SELECT id FROM professionals WHERE id = ?", (appointment.professional_id,)
    )
    profesional = cursor.fetchone()
    if not profesional:
        conexion.close()
        raise HTTPException(status_code=404, detail="Profesional no encontrado")

    # insertar el turno
    conexion.execute(
        """
        INSERT INTO appointments (professional_id, patient_name, appointment_date)
        VALUES (?, ?, ?)
        """,
        (appointment.professional_id, appointment.patient_name, appointment.appointment_date),
    )
    conexion.commit()
    conexion.close()

    return {
        "message": "Turno médico creado correctamente",
        "data": appointment.dict()
    }
