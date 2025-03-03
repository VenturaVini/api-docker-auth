import os
from fastapi.responses import FileResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_sql import get_db, UsuarioDB, criar_banco
from database.db_auth import autenticar_usuario
from security.hash import gerar_hash_senha, verificar_senha
from security.auth_handler import criar_token
from models.usuario import Usuario, NovaSenha
from service.utils.bot_telegram import enviar_mensagem

router = APIRouter()

# Criar as tabelas no banco caso ainda não existam
criar_banco()

@router.post("/register")
def registrar_usuario(usuario: Usuario, db: Session = Depends(get_db)):
    # Verifica se o usuário já existe no banco
    if db.query(UsuarioDB).filter(UsuarioDB.username == usuario.username).first():
        raise HTTPException(status_code=400, detail="Usuário já cadastrado")

    novo_usuario = UsuarioDB(username=usuario.username, senha_hash=gerar_hash_senha(usuario.senha))
    db.add(novo_usuario)
    db.commit()

    enviar_mensagem(f'Novo Usuário Cadastrado! {usuario.username}')
    return {"mensagem": "Usuário registrado com sucesso"}

@router.post("/login")
def login(usuario: Usuario, db: Session = Depends(get_db)):
    usuario_db = autenticar_usuario(usuario.username, usuario.senha, db)
    if not usuario_db:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = criar_token(usuario.username)
    enviar_mensagem(f'Usuário logado: {usuario.username}')
    #return {"access_token": token}  # normal
    # Criar um arquivo temporário com o token
    file_path = "token.txt"
    with open(file_path, "w") as f:
        f.write(token)

    return FileResponse(file_path, filename="token.txt", media_type="text/plain")


@router.post("/change_password")
def change_password(usuario: NovaSenha, db: Session = Depends(get_db)):
    usuario_db = db.query(UsuarioDB).filter(UsuarioDB.username == usuario.username).first()
    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    if not verificar_senha(usuario.senha, usuario_db.senha_hash):
        raise HTTPException(status_code=401, detail="Senha incorreta")

    usuario_db.senha_hash = gerar_hash_senha(usuario.nova_senha)
    db.commit()

    enviar_mensagem(f'Usuário alterou a senha: {usuario.username}')
    return {"mensagem": "Senha alterada com sucesso"}
