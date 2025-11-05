from fastapi import APIRouter
from chat import Message, ResponseMessage
from services.responder import get_gemini_reply
from db.seed import seed_database

app = APIRouter()

DIRECTORIO = {
    "Cardiología": ["Dr. Juan Rodríguez", "Dra. Marta Pérez"],
    "Dermatología": ["Dr. Pedro Gómez", "Dra. Ana López"],
    "Neurología": ["Dr. Luis Fernández", "Dra. María Torres"],
    "Pediatría": ["Dr. Pablo Díaz", "Dra. Laura Sánchez"],
}

@app.get("/")
def index():
    return {"message": "Bienvenido al Chatbot de la Clínica"}

@app.post("/chat/respond", response_model=ResponseMessage)
def chat_mensaje(message: Message):
    user_message = message.content.lower()

    if "especialidad" in user_message or "especialidades" in user_message:
        return {"response": f"Las especialidades disponibles son: {', '.join(DIRECTORIO.keys())}"}

    for especialidad, profesionales in DIRECTORIO.items():
        if especialidad.lower() in user_message:
            return {"response": f"Los profesionales en {especialidad} son: {', '.join(profesionales)}"}

    response = get_gemini_reply(message.content)
    return {"response": response}

@app.get("/directory/specialties")
def listar_especialidades():
    return {"specialties": list(DIRECTORIO.keys())}

@app.get("/directory/professionals/{specialty}")
def listar_profesionales(specialty: str):
    profesionales = DIRECTORIO.get(specialty, [])
    return {"specialty": specialty, "professionals": profesionales}

@app.post("/appointments")
def crear_turno_medico():
    
    return {"message": "Turno médico creado correctamente"}