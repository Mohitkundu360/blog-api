# app/routers/__init__.py

from fastapi import APIRouter
from . import auth, posts  # ✅ use relative imports

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["Auth"])
router.include_router(posts.router, prefix="/posts", tags=["Posts"])
