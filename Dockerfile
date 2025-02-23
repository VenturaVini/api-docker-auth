FROM python:3.12

WORKDIR /app

# Copia apenas os arquivos necessários primeiro (otimiza o cache do Docker)
COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt

# Agora copia todo o restante do código
COPY . . 

EXPOSE 7003

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7003"]
