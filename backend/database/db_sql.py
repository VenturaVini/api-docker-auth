from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
import os
import os
from sqlalchemy import create_engine

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)


# # Obtendo a URL do banco de dados das variáveis de ambiente
# DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://myuser:mypassword@db:5432/mydatabase")

# # Criando o engine e a sessão do SQLAlchemy
# engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo da tabela de usuários
class UsuarioDB(Base):
    __tablename__ = "usuarios"

    username = Column(String, primary_key=True, index=True)
    senha_hash = Column(String, nullable=False)

# Criando as tabelas no banco de dados
def criar_banco():
    try:
        # Tenta criar as tabelas
        Base.metadata.create_all(bind=engine)
        print("Banco de dados configurado com sucesso.")
    except OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
