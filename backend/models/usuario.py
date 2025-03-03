from pydantic import BaseModel

class Usuario(BaseModel):
    username: str
    senha: str


class NovaSenha(BaseModel):
    username: str
    senha: str
    nova_senha: str