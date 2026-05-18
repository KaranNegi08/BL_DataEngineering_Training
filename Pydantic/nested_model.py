from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address:Address
    
address_dict= {'city':'Agra', 'state':'UP', 'pin':'282007'}
address1= Address(**address_dict)

patient_dict = {'name':'KK','gender':'Male','age':20,'address':address1}
patient1 = Patient(**patient_dict)
# print(patient1.name)
# print(patient1.address.pin)

patient1.model_dump() #convert model to dict
