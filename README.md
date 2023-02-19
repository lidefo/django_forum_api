# django_forum_api

## [In English](#English-documentation) | [In Russian](#Документация-на-русском)

## English documentation

## Project description:

A full description of the project for which the API was created is presented in the repository, the link to which is below.
### [django_forum](https://github.com/lidefo/django_forum)

## Development tools:

- Python 3.10
- Django 4.1
- django-rest-framework 3.14
- PostgreSQL

## How to launch:

1) Clone repository
```
git clone "repository_link"
```

2) Create virtual environment
```
python -m venv venv
```

3) Activate virtual environment
```
venv\Scripts\activate.bat
```

4) Install requirement libraries
```
pip install -r requirements.txt
```

5) Create DataBase based on PostgreSQL

6) Fill .env.example file and rename it to ".env"

7) Apply migrations
```
python manage.py migrate
```

8) Launch server
```
python manage.py runserver
```


## Документация на русском
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
