from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DB_URL

# SQLAlchemy Declarative Mapping
Base = declarative_base()

engine = create_engine(DB_URL,
                       echo=True,  # for debug
                       connect_args={"check_same_thread": False})  # for SQLite
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
