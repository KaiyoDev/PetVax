from fastapi import APIRouter
from app.models.vaccine import Vaccine

router = APIRouter(prefix="/vaccines", tags=["Vaccines"])

vaccines = []

@router.get("/", response_model=list[Vaccine])
def get_vaccines():
    return vaccines
