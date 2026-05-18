from pydantic import BaseModel, EmailStr,field_validator, computed_field
from typing import List, Dict,Optional, Annotated

class Patient(BaseModel):
    name: str
    email:EmailStr
    age:int 
    weight:float
    height:float
    married: bool
    allergies:Optional[List[str]]=None
    contact: Dict[str,str]
    
    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight / (self.height**2),2)
        return bmi
    
   


def insert_patient(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(f"BMI: {patient.calculate_bmi}")
    print(patient.allergies)
    print('Inserted.....')
    
    
patient_info= {'name':'Nitish','email':"abc@hdfc.com",'age':30,'weight':75, "height":1.68 ,'married':True,'contact':{'email':'abc@gmail.com','phone':'7894572361'}}
patient1= Patient(**patient_info)

insert_patient(patient1)
# print(patient1.model_dump())