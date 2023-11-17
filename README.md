# nova_test

Решение тестового задания на должность Backend разработчика в компании NOVA

## Техническое задание

Сделать API метод, который можно будет запустить POST запросом с параметрами:

1. data = Текстовое содержимое файла
2. name = Название файла

Необходимо создать в Google Drive документ с названием = name и содержимым = data

Предварительно нужно создать Гугл аккаунт пустой и авторизовать приложение, чтобы получить токены

**Нужно использовать:**

- Фреймворк Django

## Стек

- Python
- Django

## Локальный запуск проекта

Клонируйте репозиторий:

```bash
git clone git@github.com:galirkil/nova-test.git
```

Перейдите в папку с проектом, установите и активируйте виртуальное окружение:

```bash
cd nova-test
python3 -m venv venv
source venv/bin/activate
```

Установите зависимости:

```bash
pip install -r requirements.txt
```

Выполните миграции:

```bash
python3 manage.py migrate
```

Добавить в рабочую директорию проекта файл с названием client_secrets.json
содержащий OAuth 2.0 Client ID приложения из Google Cloud.

Запустите сервер:

```bash
python3 manage.py runserver
```

## Описание API

**Create Gdrive file**

Создает Google Drive документ c расширением ".txt" на основе
переданных имени и содержимого.

**Endpoints**

POST http://127.0.0.1:8000/api/create-gdrive-file/

Создает Google Drive документ с переданными в теле запроса параметрами.

_Параментры_

| Параметр тела запроса | Обязательно / необязательно | Тип данных | Описание                   |
|-----------------------|-----------------------------|------------|----------------------------|
| name                  | required                    | string     | Название файла             |
| data                  | required                    | string     | Текстовое содержимое файла |


_Пример запроса_

```bash
curl --json '{"name": "some name", "data": "some data"}' http://127.0.0.1:8001/api/create-gdrive-file/
```

_Пример ответа_

```yaml
{
  "message":"File 'some name.txt' was created on google drive"
}
```

Результат: создан Google Drive документ с названием = name и содержимым = data.