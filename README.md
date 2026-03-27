# My Django App — Web Portal

> Веб-приложение на Django с фронтендом на JS/CSS, задеплоенное через Railway.

## О проекте

Полноценное веб-приложение на Python/Django. Проект включает бэкенд на Django, кастомный фронтенд и настройки для деплоя на Railway.

## Технологии

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Deploy:** Railway (`railway.json`), Dockerfile
- **Структура:** Django-проект `myportal`

## Структура проекта

```
my_django_app/
├── myportal/       # Django-приложение
├── railway.json    # Конфигурация Railway
└── Dockerfile      # Контейнеризация
```

## Установка и запуск локально

```bash
# Клонировать репозиторий
git clone https://github.com/shabunovasofia/my_django_app.git
cd my_django_app

# Создать виртуальное окружение
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Установить зависимости
pip install -r requirements.txt

# Применить миграции
python manage.py migrate

# Запустить сервер
python manage.py runserver
```

## Деплой

Проект настроен для деплоя на [Railway](https://railway.app/):

```bash
railway up
```

---

*Django-проект с деплоем на Railway.*
