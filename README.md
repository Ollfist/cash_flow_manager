# English
# Web-app "Сash flow manager"
Simple web app for cash flow management
A cash flow accounting application with support for logical dependencies between entities (Type → Category → Subcategory).

## Technology
- Python 3.x
- Django 4.x/5.x
- SQLite
- Bootstrap 5 (django-bootstrap5)

## Installation and launch

1. **Creating a virtual environment (recommended):**
```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
```

2. **Installing dependencies:**
```bash 
pip install django django-bootstrap5
```

3. **Database Setup:**
```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Creating a superuser (for accessing the admin area and filling out directories):**
```bash
python manage.py createsuperuser
```
It is recommended that you first go to /admin/ and create several Types, Statuses, Categories, and Subcategories to test dependencies.

5. **Server Startup:**
```bash
python manage.py runserver
```

6. **Access:**
Open the browser at: http://127.0.0.1:8000/
# _______________________
# Русский
# Веб-приложение "Учет ДДС"
Простое веб-приложение для управления денежными потоками
Приложение для учета движения денежных средств с поддержкой логических зависимостей между сущностями (Тип → Категория → Подкатегория).

## Технологии
- Python 3.x
- Django 4.x/5.x
- SQLite
- Bootstrap 5 (django-bootstrap5)

## Установка и запуск

1. **Создание виртуального окружения (рекомендуется):**
```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
```

2. **Установка зависимостей:**
```bash 
pip install django django-bootstrap5
```

3. **Настройка базы данных:**
```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Создание суперпользователя (для доступа к админке и заполнения справочников):**
```bash
python manage.py createsuperuser
```
Рекомендуется сначала зайти в /admin/ и создать несколько Типов, Статусов, Категорий и Подкатегорий, чтобы протестировать зависимости.

5. **Запуск сервера:**
```bash
python manage.py runserver
```


6. **Доступ:**
Откройте браузер по адресу: http://127.0.0.1:8000/