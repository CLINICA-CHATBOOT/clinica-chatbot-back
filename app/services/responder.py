# app/services/responder.py
import google.generativeai as genai
from app.config import settings

genai.configure(api_key=settings.GOOGLE_API_KEY)

# Elegí uno de estos:
# _MODEL_NAME = "gemini-flash-latest"   # rápido y económico
_MODEL_NAME = "gemini-2.5-flash"        # más capaz

_model = genai.GenerativeModel(_MODEL_NAME)

def get_gemini_reply(prompt: str) -> str:
    try:
        resp = _model.generate_content(prompt)
        return (resp.text or "").strip() or "[Sin contenido de Gemini]"
    except Exception as e:
        return f"[Gemini error] {type(e).__name__}: {e}"
