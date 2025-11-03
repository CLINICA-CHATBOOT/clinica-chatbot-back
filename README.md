🏥 Clínica Chatbot – Backend

Asistente virtual para una clínica médica.
Este servicio ofrece un chatbot que responde preguntas comunes, permite consultar profesionales y manejar turnos básicos.

📂 Estructura general del proyecto
app/
 ├── api/
 │   ├── routes/           # Endpoints (chat, profesionales, etc.)
 │   ├── db/               # Base de datos y seed inicial
 │   ├── models/           # Modelos Pydantic
 │   └── services/         # Reglas, lógica de IA y respuestas
 ├── tests/                # Pruebas unitarias
 ├── main.py               # Punto de inicio del servidor FastAPI
Dockerfile                 # Imagen para desplegar con Docker
requirements.txt           # Dependencias del backend

⚙️ Requisitos previos

Para ejecutar el proyecto podés usar dos formas:

🔹 Opción 1: instalación manual

Requiere:

Python 3.10 o superior

pip (gestor de paquetes de Python)

🔹 Opción 2: con Docker (recomendado para practicar despliegue)

Requiere:

Docker Desktop o Docker Engine instalado

Conexión a internet para descargar la imagen base

🚀 Configuración inicial (modo local)

1️⃣ Clonar el repositorio:

git clone https://github.com/CLINICA-CHATBOOT/clinica-chatbot-back.git
cd clinica-chatbot-back


2️⃣ Crear un entorno virtual e instalar dependencias:

python -m venv venv
source venv/Scripts/activate  # (en Windows)
# o source venv/bin/activate   # (en Linux/Mac)
pip install -r requirements.txt


3️⃣ (Opcional) Crear archivo .env (si no existe):

DB_URL=sqlite:///./clinicadb.sqlite3
GEMINI_API_KEY=tu_api_key_aqui


4️⃣ Ejecutar el servidor:

uvicorn app.main:app --reload


📍 Servidor disponible en:
http://127.0.0.1:8000

Documentación interactiva: http://127.0.0.1:8000/docs

🐳 Ejecución con Docker

1️⃣ Construir la imagen:

docker build -t clinica-chatbot-back .


2️⃣ Crear y ejecutar el contenedor:

docker run -d -p 8000:8000 --name chatbot clinica-chatbot-back


3️⃣ Verificar que esté activo:

docker ps


4️⃣ Acceder desde el navegador:
http://localhost:8000/docs

🧠 Integración con IA (Gemini)

El chatbot utiliza Gemini AI como respaldo cuando no reconoce una intención.

Para habilitarlo:

Crear una cuenta en Google AI Studio
.

Copiar la API Key.

Guardarla en el archivo .env:

GEMINI_API_KEY=tu_api_key


La clase encargada de procesar esto está en app/services/responder.py.

🧱 Base de datos

Motor: SQLite (archivo local clinicadb.sqlite3)

Ubicación: raíz del proyecto (puede cambiarse por Postgres modificando DB_URL)

Tablas principales:

specialties → especialidades médicas

professionals → listado de profesionales

appointments → turnos (opcional)

Carga inicial (seed): automática al iniciar el proyecto (app/db/seed.py)

🔍 Endpoints principales
Método	Ruta	Descripción
GET	/	Verifica que la API esté activa
POST	/chat/respond	Envía mensaje del usuario y recibe respuesta del chatbot
GET	/directory/specialties	Lista las especialidades disponibles
GET	/directory/professionals	Lista o busca profesionales
POST	/appointments	Crea un turno médico (si está implementado)
🧪 Ejemplos de uso con curl

Probar el chat:

curl -X POST http://127.0.0.1:8000/chat/respond \
     -H "Content-Type: application/json" \
     -d '{"text":"Necesito un cardiólogo"}'


Listar especialidades:

curl http://127.0.0.1:8000/directory/specialties

🧰 Scripts útiles
Comando	Descripción
uvicorn app.main:app --reload	Ejecutar servidor local
pytest	Ejecutar tests automáticos
docker build -t clinica-chatbot-back .	Crear imagen Docker
docker run -p 8000:8000 clinica-chatbot-back	Ejecutar contenedor
🧩 Flujo de desarrollo (GitFlow simple)

Todos los cambios se hacen en ramas feature/... a partir de develop.

Se hacen Pull Requests hacia develop.

Solo versiones estables se fusionan a main.

main está protegida (no se puede pushear directo).

👥 Equipo
Rol	                    Nombre	               
Coordinador técnico	    Federico Musa	
Desarrolladora  	    Tamara Paez	
💡 Notas finales

El objetivo del proyecto es educativo: practicar trabajo en equipo, manejo de ramas, integración IA y despliegue con Docker.

El código busca ser claro, reproducible y sin dependencias innecesarias.

Puede expandirse fácilmente con un front React o una app de escritorio.