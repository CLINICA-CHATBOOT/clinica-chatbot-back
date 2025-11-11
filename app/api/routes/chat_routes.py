# -*- coding: utf-8 -*-
from fastapi import APIRouter
from app.models.chat import Message, ResponseMessage
from app.services.responder import get_gemini_reply

router = APIRouter()

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

    if "especialidad" in user_message or "especialidades" in user_message:
        lista = "\n - " + "\n - ".join(DIRECTORIO.keys())
        return {"response": f"Las especialidades disponibles son:\n{lista}"}
    
    for especialidad, profesionales in DIRECTORIO.items():
        lista = "\n - " + "\n - ".join(profesionales)
        return {"response": f"Los profesionales en {especialidad} son:\n{lista}"}

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
def crear_turno_medico():
    # seed_database()
    return {"message": "Turno médico creado correctamente"}
# -*- coding: utf-8 -*-
@router.get("/directory/specialties")
def listar_especialidades():
    return {"specialties": list(DIRECTORIO.keys())}

@router.get("/directory/professionals/{specialty}")
def listar_profesionales(specialty: str):
    profesionales = DIRECTORIO.get(specialty, [])
    return {"specialty": specialty, "professionals": profesionales}

@router.post("/appointments")
def crear_turno_medico():
    # seed_database()  # si lo querés usar acá
    return {"message": "Turno médico creado correctamente"}
