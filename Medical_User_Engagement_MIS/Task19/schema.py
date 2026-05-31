from pydantic import BaseModel
from typing import Optional


class PatientCreate(BaseModel):
    patient_id:int
    fname: str
    lname: str
    age: int
    gender: str
    email: str
    phone: str
    city: str


class PatientResponse(BaseModel):
    patient_id: int
    fname: str
    lname: str
    age: Optional[int]
    gender: Optional[str]
    email: str
    phone: str
    city: str

    class Config:
        from_attributes = True