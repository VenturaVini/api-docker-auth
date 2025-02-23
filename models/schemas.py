from pydantic import BaseModel
from typing import Optional


# Schema para criar um novo usuário (entrada)
class UsuarioCreate(BaseModel):
    username: str
    senha: str
    id_telegram: int


# Schema para exibir um usuário (saída)
class UsuarioResponse(BaseModel):
    id: int
    username: str
    id_telegram: int

    class Config:
        from_attributes = True


# Schema para criar um novo produto (entrada)
class ProdutoCreate(BaseModel):
    nome: str
    descricao: str
    preco: float
    estoque: int


# Schema para exibir um produto (saída)
class ProdutoResponse(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float
    estoque: int

    class Config:
        from_attributes = True
