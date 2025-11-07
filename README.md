🏥 Clínica Chatbot – Backend

Asistente virtual para una clínica médica.
Este servicio ofrece un chatbot que responde preguntas frecuentes, permite consultar profesionales y gestionar turnos básicos.

📁 Estructura del proyecto
app/
 ├── api/
 │   ├── routes/         # Endpoints (chat, profesionales, etc.)
 │   ├── db/             # Base de datos y seed inicial
 │   ├── models/         # Modelos Pydantic
 │   └── services/       # Lógica de IA y reglas de negocio
 ├── tests/              # Pruebas unitarias
 ├── main.py             # Punto de inicio del servidor FastAPI
Dockerfile               # Imagen para despliegue con Docker
requirements.txt         # Dependencias del backend

⚙️ Requisitos previos

Podés ejecutar el proyecto de dos formas:

🔹 Opción 1 — Instalación manual

Requiere:

Python 3.10+

pip (gestor de paquetes de Python)

🔹 Opción 2 — Con Docker (recomendado)

Requiere:

Docker Desktop o Docker Engine

Conexión a internet para descargar la imagen base

🚀 Configuración inicial (modo local)

1️⃣ Clonar el repositorio:

git clone https://github.com/CLINICA-CHATBOOT/clinica-chatbot-back.git
cd clinica-chatbot-back


2️⃣ Crear entorno virtual e instalar dependencias:

python -m venv venv
source venv/Scripts/activate   # Windows
# o
source venv/bin/activate       # Linux/Mac

pip install -r requirements.txt


3️⃣ (Opcional) Crear archivo .env:

DB_URL=sqlite:///./clinicadb.sqlite3
GEMINI_API_KEY=tu_api_key_aqui


4️⃣ Ejecutar el servidor:

uvicorn app.main:app --reload


📍 Servidor disponible en:
👉 http://127.0.0.1:8000

📘 Documentación interactiva: http://127.0.0.1:8000/docs

🐳 Ejecución con Docker

1️⃣ Construir la imagen:

docker build -t clinica-chatbot-back .


2️⃣ Crear y ejecutar el contenedor:

docker run -d -p 8000:8000 --name chatbot clinica-chatbot-back


3️⃣ Verificar estado:

docker ps


4️⃣ Acceder desde navegador:
👉 http://localhost:8000/docs

🧠 Integración con IA (Gemini)

El chatbot utiliza Gemini AI como respaldo cuando no reconoce la intención del usuario.

Pasos para habilitarlo:

Crear cuenta en Google AI Studio

Obtener la API Key.

Guardarla en el .env:

GEMINI_API_KEY=tu_api_key


📄 Código responsable:
app/services/responder.py

🧱 Base de datos

Motor: SQLite (clinicadb.sqlite3)

Ubicación: raíz del proyecto (puede cambiarse por Postgres editando DB_URL)

Tablas principales:

Tabla	Descripción
specialties	Especialidades médicas
professionals	Listado de profesionales
appointments	Turnos (opcional)

🔸 Carga inicial (seed): automática al iniciar el proyecto
📍 Archivo: app/db/seed.py

🔍 Endpoints principales
Método	Ruta	Descripción
GET	/	Verifica que la API esté activa
POST	/chat/respond	Envía mensaje del usuario y recibe respuesta
GET	/directory/specialties	Lista especialidades disponibles
GET	/directory/professionals	Lista o busca profesionales
POST	/appointments	Crea turno médico (si está implementado)
🧪 Ejemplos de uso (curl)

Probar el chat:

curl -X POST http://127.0.0.1:8000/chat/respond \
     -H "Content-Type: application/json" \
     -d '{"text":"Necesito un cardiólogo"}'


Listar especialidades:

curl http://127.0.0.1:8000/directory/specialties

🧰 Comandos útiles
Comando	Descripción
uvicorn app.main:app --reload	Ejecutar servidor local
pytest	Ejecutar tests
docker build -t clinica-chatbot-back .	Crear imagen Docker
docker run -p 8000:8000 clinica-chatbot-back	Ejecutar contenedor
🧩 Flujo de desarrollo (GitFlow)

Cada cambio parte de una rama feature/... desde develop.

Se crean Pull Requests hacia develop.

Solo versiones estables se fusionan a main.

main está protegida (no se puede pushear directamente).

👥 Equipo
Rol	Nombre
Coordinador técnico	Federico Musa
Desarrolladora	Tamara Páez
💡 Notas finales

El objetivo del proyecto es educativo: practicar trabajo en equipo, ramas, integración con IA y despliegue con Docker.
El código busca ser claro, reproducible y modular, facilitando futuras ampliaciones (por ejemplo, front en React o app de escritorio).