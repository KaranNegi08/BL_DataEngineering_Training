from pydantic import BaseModel, EmailStr,field_validator, model_validator
from typing import List, Dict,Optional, Annotated

# class Patient(BaseModel):
#     name: str
#     email:EmailStr
#     age:int 
#     weight:float
#     married: bool
#     allergies:Optional[List[str]]=None
#     contact: Dict[str,str]
    
#     @model_validator(mode='after')
#     def validate_emergency_contact(self):
#         if self.age >60 and 'emergency' not in self.contact:
#             raise ValueError("Patients older than 60 must have an emergency number.")
    

class Transfer(BaseModel):
    balance :float
    transfer_amount:float
    
    @model_validator(mode='after')
    def check_balance(self):
        if self.transfer_amount > self.balance:
            raise ValueError("Insufficient Balance..")
        return self
    
def check(model:Transfer):
    print(model.balance)
    print(model.transfer_amount)


# def insert_patient(patient:Patient):
#     print(patient.name)
#     print(patient.email)
#     print(patient.age)
#     print(patient.weight)
#     print(patient.allergies)
#     print('Inserted.....')
    
    
# patient_info= {'name':'Nitish','email':"abc@hdfc.com",'age':70,'weight':75, 'married':True,'contact':{'email':'abc@gmail.com','phone':'7894572361','emergency':'897945789'}}
# patient1= Patient(**patient_info)

# insert_patient(patient1)
# print(patient1.model_dump())
info = {"balance":10000,"transfer_amount": 5000}

t= Transfer(**info)
check(t)
