# FastAPI SQLAlchemy Alembic

Example project using FastAPI, SQLAlchemy and Alembic.

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
