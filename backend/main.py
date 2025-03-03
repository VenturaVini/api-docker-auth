import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Importar o middleware
from routes import auth, produtos

app = FastAPI()

# Adicionando o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens (cuidado em produção)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos os headers
)

# Incluindo as rotas
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(produtos.router, tags=["Produtos"])

@app.get("/env")
def read_env():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")
    SECRET_KEY = os.getenv('SECRET_KEY')
    return {
        "BOT_TOKEN": BOT_TOKEN,
        "CHAT_ID": CHAT_ID,
        "SECRET_KEY": SECRET_KEY
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 7200))
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
