from pydantic import BaseModel
from typing import Optional

class Pet(BaseModel):
    id: int
    name: str
    age: int
    species: str  
    owner_id: int 
    vaccinated: bool
