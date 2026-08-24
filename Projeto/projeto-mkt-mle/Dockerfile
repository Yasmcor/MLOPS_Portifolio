# 1. Usa a imagem Python padrão
FROM python:3.11-slim

# 2. Define o diretório de trabalho
WORKDIR /app

# 3. Copia os requisitos e instala TUDO
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install uvicorn fastapi --no-cache-dir

# 4. Copia o código da aplicação (app.py, src/, model/, data/)
COPY app.py .
COPY src/ src/
COPY model/ model/
COPY data/ data/

# 5. Expõe a porta que o FastAPI vai rodar
EXPOSE 8000

# 6. Comando de execução (Corrigido para usar o módulo Python, o que resolve o erro)
CMD ["python", "-m", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
