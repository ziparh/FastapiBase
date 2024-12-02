from fastapi import APIRouter
from app.core import settings

router = APIRouter(prefix=settings.prefix.api)
# router.include_router()