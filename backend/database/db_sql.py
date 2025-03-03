from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Obtendo a URL do banco de dados das variáveis de ambiente
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://myuser:mypassword@db:5432/mydatabase")

# Criando o engine e a sessão do SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo da tabela de usuários
class UsuarioDB(Base):
    __tablename__ = "usuarios"

    username = Column(String, primary_key=True, index=True)
    senha_hash = Column(String, nullable=False)

# Criando as tabelas no banco de dados
def criar_banco():
    Base.metadata.create_all(bind=engine)

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
