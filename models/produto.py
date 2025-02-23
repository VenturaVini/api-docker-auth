from sqlalchemy import Column, Integer, String, Float
from database.db import Base

class Produto(Base):
    __tablename__ = "produtos"
    __table_args__ = {"extend_existing": True}  # Adiciona essa linha

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)
