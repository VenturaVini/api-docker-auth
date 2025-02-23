import logging
import psycopg2
from urllib.parse import quote
from sqlalchemy import create_engine, Column, Integer, String, Text, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Credenciais do banco
DB_USER = "usuario_produto"
DB_PASSWORD = "qweasd12"
DB_HOST = "db"
DB_PORT = "5432"
DB_NAME = "banco_produtos"

# Escapar senha
DB_PASSWORD_ESCAPED = quote(DB_PASSWORD)

# Conectar ao PostgreSQL sem especificar o banco
DATABASE_URL_BASE = f"postgresql://{DB_USER}:{DB_PASSWORD_ESCAPED}@{DB_HOST}:{DB_PORT}/postgres"

def criar_banco():
    """Cria o banco de dados caso ele não exista."""
    try:
        conn = psycopg2.connect(DATABASE_URL_BASE)
        conn.autocommit = True
        cursor = conn.cursor()

        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'")
        if not cursor.fetchone():
            cursor.execute(f"CREATE DATABASE {DB_NAME} WITH ENCODING 'UTF8' TEMPLATE template0;")
            logger.info(f"✅ Banco '{DB_NAME}' criado com sucesso!")
        else:
            logger.info(f"✅ Banco '{DB_NAME}' já existe.")
    except Exception as e:
        logger.error(f"❌ Erro ao criar o banco: {e}")
    finally:
        cursor.close()
        conn.close()

# Agora conecta ao banco correto
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD_ESCAPED}@{DB_HOST}:{DB_PORT}/{DB_NAME}?client_encoding=utf8"
engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)

# Criando sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criando base de modelos
Base = declarative_base()

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
