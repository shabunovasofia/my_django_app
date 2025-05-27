FROM python:3.10

WORKDIR /myportal

# Копируем файл из myportal внутрь образа
COPY myportal/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё содержимое myportal внутрь контейнера
COPY myportal .

EXPOSE 8000

CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "myportal.asgi:application"]
