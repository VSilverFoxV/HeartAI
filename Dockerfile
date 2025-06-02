FROM python:3.12-slim

WORKDIR /app

# Установка необходимых зависимостей для сборки
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    gfortran \
    libopenblas-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip

# Копирование файлов зависимостей
COPY requirements.txt .

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование файлы веб-приложения
COPY run.py .
COPY website/ ./website/

# Создание директории для модели
RUN mkdir -p heart_neural_network

# Команда для запуска приложения
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "website.app:app"]

# Порт, на котором работает приложение
EXPOSE 8000 