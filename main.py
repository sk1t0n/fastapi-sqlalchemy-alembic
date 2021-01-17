from fastapi import FastAPI
import uvicorn

from core import config
from api.routes import router

# Create database tables: alembic upgrade head

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(
    title=config.PROJECT_NAME,
    description=config.PROJECT_DESCRIPTION,
    version=config.PROJECT_VERSION,
    openapi_tags=tags_metadata,
    openapi_url=f"{config.API_V1_STR}/openapi.json"
)
app.include_router(router, prefix=config.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, debug=True)
