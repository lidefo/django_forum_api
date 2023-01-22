# django_forum_api

## Описание проекта:

Полное описание проекта, для которого создавалось API, представлено в репозитории, ссылка на который ниже.
### [django_forum](https://github.com/lidefo/django_forum)

## Инструменты разработки:

- Python 3.10
- Django 4.1
- django-rest-framework 3.14
- PostgreSQL

## Запуск проекта:

1) Клонировать репозиторий.
```
git clone ссылка_на_репозиторий
```
2) Создать виртуальное окружение
```
python -m venv venv
```

3) Активировать виртуальное окружение

4) Установить необходимые пакеты
```
pip install -r requirements.txt
```

5) Создать базу данных PostreSQL

6) Заполнить файл .env.example и переименовать его в .env

7) Выполнить миграции
```
python manage.py migrate
```

8) Запустить сервер

```
python manage.py runserver
```
