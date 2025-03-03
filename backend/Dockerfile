# Usa a imagem oficial do Python como base
FROM python:3.11

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os arquivos do projeto para o contêiner
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 8000 para acesso externo
EXPOSE 7200

# Comando para rodar a API
#CMD ["uvicorn", "teste_api:app", "--host", "0.0.0.0", "--port", "7000"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7200"]

