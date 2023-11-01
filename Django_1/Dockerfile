# Используем базовый образ Python с установленным Django
FROM python:3.11

# Устанавливаем переменную окружения для отключения вывода буферизации Python
ENV PYTHONUNBUFFERED 1

# Создаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Копируем все файлы из текущей директории в контейнер
COPY Django_1 /app/

# Определяем порт, на котором будет работать приложение
EXPOSE 8000

# Команда для запуска Django сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
