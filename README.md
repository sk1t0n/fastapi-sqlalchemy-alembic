# FastAPI SQLAlchemy Alembic

Example project using FastAPI, SQLAlchemy and Alembic.

## Setup project

```sh
pipenv install
pipenv install --dev # optionally
pipenv shell
alembic upgrade head
```

## Start project

```sh
python main.py
```

## API Documentation

`http://127.0.0.1:8000/api/v1/docs`

## Alembic

Create migration:

```sh
alembic revision --autogenerate -m "Migration description"
```

Apply migration:

```sh
alembic upgrade head
```
