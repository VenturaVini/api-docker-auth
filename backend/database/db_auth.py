from sqlalchemy.orm import Session
from security.hash import verificar_senha
from database.db_sql import UsuarioDB

def autenticar_usuario(username: str, senha: str, db: Session):
    usuario_db = db.query(UsuarioDB).filter(UsuarioDB.username == username).first()
    if not usuario_db or not verificar_senha(senha, usuario_db.senha_hash):
        return None
    return usuario_db