# образ йоу
FROM python:3.11-slim

# установка мейн директории
WORKDIR /app

# копирование зависимостей
COPY requirements.txt .

# установка зависимостей
RUN pip install -r requirements.txt

# копирование кода
COPY . .

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0","--port", "8000", "--workers", "4" ]