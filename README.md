# FastAPI SQLAlchemy Alembic

## Alembic

Create migration:

```sh
alembic revision --autogenerate -m "Migration description"
```

Apply migration:

```sh
alembic upgrade head
```
