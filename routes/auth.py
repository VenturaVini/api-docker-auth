from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from security.hash import gerar_hash_senha, verificar_hash_senha
from security.auth_token import criar_token
from database.db import get_db
from models.login import Usuario
from service.bot_telegram import enviar_mensagem
from models.schemas import UsuarioCreate, UsuarioResponse

router = APIRouter()


@router.post("/register", response_model=UsuarioResponse)
def registrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_existente = db.query(Usuario).filter(Usuario.username == usuario.username).first()

    if usuario_existente:
        raise HTTPException(status_code=400, detail="Usuário já cadastrado!")

    novo_usuario = Usuario(
        username=usuario.username,
        senha=gerar_hash_senha(usuario.senha),
        id_telegram=usuario.id_telegram,
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    enviar_mensagem(f"Usuário: {usuario.username}, cadastrado com sucesso no sistema!")

    return novo_usuario  # Retorna o modelo SQLAlchemy que será convertido pelo Pydantic


@router.post("/login")
def login(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_db = db.query(Usuario).filter(Usuario.username == usuario.username).first()

    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuário não está cadastrado no banco de dados!")

    if not verificar_hash_senha(usuario.senha, usuario_db.senha):
        raise HTTPException(status_code=401, detail="Senha incorreta!")

    token = criar_token(usuario.username)
    enviar_mensagem(f"Usuário logado no sistema: {usuario.username}")

    return {"Token": token}
