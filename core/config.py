DB_NAME = "fastapi_sqlalchemy_alembic"
DB_URL = f"sqlite:///{DB_NAME}.db"

USERS_PER_PAGE = 5
ITEMS_PER_PAGE = 5

PROJECT_NAME = "FastAPI SQLAlchemy Alembic"
PROJECT_DESCRIPTION = "An example of FastAPI working with SQLAlchemy and Alembic"
PROJECT_VERSION = "0.1.0"
API_V1_STR = "/api/v1"

# JWT, хранить все секретные данные в переменных среды или .env-файле
# для генерации ключа ввести: openssl rand -hex 32
SECRET_KEY = "a446bbe560387c016dad039ccd88a267c9cae0bf886c59387a416f1c1a397c05"
ALGORITHM = "HS256"  # симметричное шифрование, один ключ на бэкенде и фронтенде
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # время действия токена в минутах
