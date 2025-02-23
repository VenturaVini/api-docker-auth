import os
from dotenv import load_dotenv
import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, Header


# Carrega o .env somente se estiver rodando localmente
if os.getenv('RAILWAY_ENVIRONMENT') is None:
    load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

algorithm="HS256"


def criar_token(username: str):

    payload = {
        "sub": username,
        "expiration": datetime.utcnow() + timedelta(hours=0.025)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm)


def verificar_token(token: str):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithm)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token Expirado!')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=404, detail='Token Invalido!')
    

def obter_usuario_logado(Authorizador: str):
    token = Authorizador
    return verificar_token(token)