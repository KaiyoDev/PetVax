from fastapi import APIRouter
router = APIRouter()

@router.get("/pets")
def get_pets():
    return [{"id": 1, "name": "Vang"}, {"id": 2, "name": "Den"}]

@router.post("/pets")
def add_pet(pet: dict):
    return {"message": "Pet added successfully", "pet": pet}
