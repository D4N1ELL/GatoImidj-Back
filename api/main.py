"""API routes."""

from fastapi import APIRouter
from .health import router as health_router
from .routes.cookies import router as cookies_router
from .routes.memes import router as memes_router
from .routes.users import router as users_router
from .routes.likes import router as likes_router
from .routes.auth import router as auth_router

router = APIRouter()


router.include_router(health_router)
router.include_router(cookies_router)
router.include_router(memes_router)
router.include_router(users_router)
router.include_router(likes_router)
router.include_router(auth_router)