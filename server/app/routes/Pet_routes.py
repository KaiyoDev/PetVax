from fastapi import APIRouter
from app.models.pet import Pet

router = APIRouter(prefix="/pets", tags=["Pets"])

# Fake DB (demo)
pets = []

@router.get("/", response_model=list[Pet])
def get_pets():
    return pets

@router.post("/", response_model=Pet)
def create_pet(pet: Pet):
    pets.append(pet)
    return pet

@router.get("/{pet_id}", response_model=Pet)
def get_pet(pet_id: int):
    for pet in pets:
        if pet.id == pet_id:
            return pet
    return {"error": "Pet not found"}
