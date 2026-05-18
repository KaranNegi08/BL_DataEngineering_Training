from pydantic import BaseModel, EmailStr,AnyUrl, Field
from typing import List, Dict,Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50, title="Name of the Patient", description="The name of the patient should be less than 50", examples=['Nitish','Amit'])]
    email:EmailStr
    linkedin_url:AnyUrl
    age:int = Field(gt=0, lt=120)
    weight:Annotated[float, Field(gt=0,strict=True)]
    married: bool=False
    allergies:Optional[List[str]]=None
    contact: Dict[str,str]


def insert_patient(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.allergies)
    print('Inserted.....')
    
    
patient_info= {'name':'Nitish','linkedin_url':'http://linkedin.com/KaranNegi','email':"abc@gmail.com",'age':30,'weight':75, 'married':True,'contact':{'email':'abc@gmail.com','phone':'7894572361'}}
patient1= Patient(**patient_info)

insert_patient(patient1)