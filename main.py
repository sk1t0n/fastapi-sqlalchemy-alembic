from fastapi import FastAPI
import uvicorn

from endpoints import router

# Create database tables: alembic upgrade head

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, debug=True)
