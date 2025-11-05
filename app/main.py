from fastapi import FastAPI
from app.api.routes.chat_routes import router as chat_router

app = FastAPI()

# monta el router en /api
app.include_router(chat_router, prefix="/api")

@app.get("/health")
def health():
    return {"status": "ok"}
