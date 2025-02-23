from passlib.context import CryptContext

encriptador_senha = CryptContext(schemes=['bcrypt'], deprecated='auto')


def gerar_hash_senha(senha: str):
    return encriptador_senha.hash(senha)


def verificar_hash_senha(senha: str, hash_senha: str):
    return encriptador_senha.verify(secret=senha, hash=hash_senha)

