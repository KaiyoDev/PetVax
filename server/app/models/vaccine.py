from pydantic import BaseModel

class Vaccine(BaseModel):
    id: int
    name: str
    manufacturer: str
    required_doses: int
