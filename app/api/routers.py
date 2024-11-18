from fastapi import APIRouter

from .endpoints import rate_router

main_router = APIRouter()
main_router.include_router(
    rate_router, prefix='/rate', tags=['rate']
)
