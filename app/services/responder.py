import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def get_gemini_reply(message: str) -> str:
    try:
        API_KEY = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash')
    except:
        message = ("Error al configurar la API de Gemini")
    return message
