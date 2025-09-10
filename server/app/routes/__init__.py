from fastapi import APIRouter
from .pet_routes import router as pet_router
from .vaccine_routes import router as vaccine_router
api_router = APIRouter()
api_router.include_router(pet_router)
api_router.include_router(vaccine_router)
