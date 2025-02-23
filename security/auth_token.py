import os
from dotenv import load_dotenv
import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, Header

# Carrega o .env se estiver rodando localmente
if os.getenv('RAILWAY_ENVIRONMENT') is None:
    load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

if SECRET_KEY is None:
    raise ValueError("SECRET_KEY não foi encontrada no ambiente. Verifique seu .env ou variáveis de ambiente.")

algorithm = "HS256"

def criar_token(username: str):
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(minutes=15)  # Alterado para 15 minutos
    }
    return jwt.encode(payload, SECRET_KEY, algorithm)

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[algorithm])  # Corrigido para 'algorithms'
        return payload['sub']
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token Expirado!")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token Inválido!")

def obter_usuario_logado(Authorization: str = Header(...)):
    if not Authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Formato de token inválido")
    
    token = Authorization.split(" ")[1]  # Pega apenas o token
    return verificar_token(token)
