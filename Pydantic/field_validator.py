from pydantic import BaseModel, EmailStr,field_validator
from typing import List, Dict,Optional, Annotated

class Patient(BaseModel):
    name: str
    email:EmailStr
    age:int 
    weight:float
    married: bool
    allergies:Optional[List[str]]=None
    contact: Dict[str,str]
    
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains= ['hdfc.com', 'icici.com']
        domain_name= value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain.")

    @field_validator('name')
    @classmethod
    def transform_name(cls,value):
        return value.upper()


def insert_patient(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print('Inserted.....')
    
    
patient_info= {'name':'Nitish','email':"abc@hdfc.com",'age':30,'weight':75, 'married':True,'contact':{'email':'abc@gmail.com','phone':'7894572361'}}
patient1= Patient(**patient_info)

insert_patient(patient1)
# print(patient1.model_dump())