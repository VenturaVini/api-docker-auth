from sqlalchemy import Column, Integer, String
from database.db import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    __table_args__ = {"extend_existing": True}  # Adiciona essa linha

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    id_telegram = Column(Integer, nullable=False)
