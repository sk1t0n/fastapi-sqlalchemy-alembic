from fastapi import APIRouter

from .endpoints import users, items, login

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(items.router, prefix="/items", tags=["items"])
router.include_router(login.router, tags=["login"])
