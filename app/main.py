from fastapi import FastAPI
from api.routes import chat

app = FastAPI()

app.include_router(chat.app, prefix="/chatbot", tags=["Chat"])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)