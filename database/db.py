import logging
from sqlalchemy import create_engine, Column, Integer, String, Text, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Definição das credenciais do banco
DB_USER = "usuario_produto"
DB_PASSWORD = "qweasd12"
DB_HOST = "db"  # Nome do serviço no Docker Compose
DB_PORT = "5432"
DB_NAME = "banco_produtos"

# Conectar ao PostgreSQL sem especificar o banco
DATABASE_URL_BASE = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/postgres"

def criar_banco():
    """Cria o banco de dados caso ele não exista."""
    try:
        conn = psycopg2.connect(DATABASE_URL_BASE)
        conn.autocommit = True
        cursor = conn.cursor()

        # Verifica se o banco já existe
        cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{DB_NAME}'")
        existe = cursor.fetchone()

        if not existe:
            cursor.execute(f"CREATE DATABASE {DB_NAME}")
            logger.info(f"✅ Banco '{DB_NAME}' criado com sucesso!")
            return True
        else:
            logger.info(f"✅ Banco '{DB_NAME}' já existe.")
            return False

    except Exception as e:
        logger.error(f"❌ Erro ao criar o banco: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

# Agora conecta ao banco correto
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)

# Criando sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criando base de modelos
Base = declarative_base()

# Modelo de Produtos no banco
class ProdutoDB(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(Text)
    preco = Column(Numeric(10, 2), nullable=False)
    estoque = Column(Integer, nullable=False)

def criar_tabelas():
    """Cria as tabelas no banco de dados."""
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("✅ Tabelas criadas com sucesso!")
    except Exception as e:
        logger.error(f"❌ Erro ao criar tabelas: {e}")

def get_db():
    """Obtém uma sessão do banco de dados."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
