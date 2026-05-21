from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional

class Patient(BaseModel):
    
    id:Annotated[str, Field(... , description='ID of the patient', examples=['P001'])]
    name:Annotated[str, Field(... , description='Name of the Patient')]
    city:Annotated[str, Field(... , description='City where the patient is living')]
    age:Annotated[int, Field(... , gt=0 , l=120, description='Age of the Patient')]
    gender:Annotated[Literal['Male','Female','others'], Field(... , description='Gender of the Patient')]
    height_cm:Annotated[float, Field(... , gt=0, description='Height of the Patient in cm')]
    weight_kg:Annotated[float, Field(... , gt=0, description='Weight of the Patient in kg')]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi= round(self.weight_kg / ((self.height_cm/100) ** 2), 2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi<25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'


class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['Male','Female','others']], Field(default=None)]
    height_cm: Annotated[Optional[float], Field(default=None, gt=0)]
    weight_kg: Annotated[Optional[float], Field(default=None, gt=0)]
