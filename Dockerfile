FROM python:3.9-alpine

# необязательные поля
LABEL "homework"="Otus"
LABEL "creator"="Klim"

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Обновляем пакеты и устанавливаем bash
RUN apk update && apk upgrade && apk add bash

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . .

# Устанавливаем команду по умолчанию для запуска тестов
CMD ["sh", "-c", "pytest --browser ${BROWSER} --alluredir=/app/allure-results"]

#docker build -t automation-tests .
#docker run --rm -e BROWSER=firefox automation-tests

