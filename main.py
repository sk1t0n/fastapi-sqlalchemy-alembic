from fastapi import FastAPI
import uvicorn

from endpoints import router

import models
from database import engine

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, debug=True)
