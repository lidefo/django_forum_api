# API documentation.

# In russian

## Пользователи:

### GET  /api/v1/profiles/ - получить список пользователей

#### Запрос 
```
GET http://127.0.0.1:8000/api/v1/profiles/
```

#### Ответ
```
{
        "id": 2,
        "last_login": null,
        "first_name": "Tester",
        "last_name": "",
        "username": "test",
        "email": "test@gmail.com",
        "register_date": "2023-01-06",
        "is_admin": false,
        "is_active": true
    },
    {
        "id": 3,
        "last_login": "2023-01-05T23:39:44.707772+03:00",
        "first_name": "",
        "last_name": "",
        "username": "admin",
        "email": "admin@admin.com",
        "register_date": "2023-01-06",
        "is_admin": true,
        "is_active": true
    }
```

### POST /api/v1/profiles/ - создать нового пользователя

#### Запрос
```
POST /api/v1/profiles/

{
    "username": "example",
    "email": "example@example.com",
    "password": "forexample",
    "first_name": "Justin",
    "last_name": "Forexample"
}
```

#### Ответ
```
{
    "id": 4,
    "last_login": null,
    "first_name": "Justin",
    "last_name": "Forexample",
    "username": "example",
    "email": "example@example.com",
    "register_date": "2023-01-11",
    "is_admin": false,
    "is_active": true
}
```

### GET /api/v1/profiles/id/

#### Запрос
```
GET http://127.0.0.1:8000/api/v1/profiles/4/
```

#### Ответ

```
{
    "id": 4,
    "last_login": null,
    "first_name": "Justin",
    "last_name": "Forexample",
    "username": "example",
    "email": "example@example.com",
    "register_date": "2023-01-11",
    "is_admin": false,
    "is_active": true
}
```

### PUT/PATCH /api/v1/profiles/id/

#### Запрос

```
PATCH http://127.0.0.1:8000/api/v1/profiles/4/
HEAD {"Authorization": "Token dd2db949c1d6a08d62390d5d68b4b28d7cdc4767"}

{
    "last_name": "Johnson"
}
```

#### Ответ

```
{
    "id": 4,
    "last_login": null,
    "first_name": "Justin",
    "last_name": "Johnson",
    "username": "example",
    "email": "example@example.com",
    "register_date": "2023-01-11",
    "is_admin": false,
    "is_active": true
}
```

### DELETE /api/v1/profiles/id/

#### Запрос

```
DELETE /api/v1/profiles/4/
HEAD {"Authorization": "Token dd2db949c1d6a08d62390d5d68b4b28d7cdc4767"}
```

#### Ответ
```


```
(Объект удалён)

## Аналогичным образом всё работает для тредов и сообщений(topics, messages).

### Получить все API роуты можно благодаря запросу, показанному ниже.

#### Запрос

```
GET http://127.0.0.1:8000/api/v1/
```

#### Ответ

```
{
    "profiles": "http://127.0.0.1:8000/api/v1/profiles/",
    "login": "http://127.0.0.1:8000/api/v1/login/",
    "topics": "http://127.0.0.1:8000/api/v1/topics/",
    "messages": "http://127.0.0.1:8000/api/v1/messages/"
}
```

## Авторизация

### Авторизация реализована через токены, токен можно получить благодаря запросу, указанному ниже.

#### Запрос

```
POST http://127.0.0.1:8000/api/v1/login/

{
    "username": "example@example.com",
    "password": "forexample"
}
```

#### Ответ

```
{
    "token": "dd2db949c1d6a08d62390d5d68b4b28d7cdc4767"
}
```