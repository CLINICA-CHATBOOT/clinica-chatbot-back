from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.routes.chat_routes import router as chat_router

app = FastAPI()

# monta el router en /api
app.include_router(chat_router, prefix="/api")

@app.get("/health")
def health():
    return {"status": "ok"}

# Montar archivos estáticos (CSS, JS, imágenes)
app.mount("/Assets", StaticFiles(directory="../clinica-chatbot-front/app/Assets"), name="assets")

# Configurar plantillas HTML
templates = Jinja2Templates(directory="../clinica-chatbot-front/app/Templates")

# Ruta principal que devuelve index.html
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})