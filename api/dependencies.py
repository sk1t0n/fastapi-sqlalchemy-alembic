from typing import Generator

from db import Session


def get_db() -> Generator:
    db = Session()
    try:
        yield db
    finally:
        db.close()
