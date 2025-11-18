from pydantic import BaseModel

class Address(BaseModel):
  
  city: str
  state: str
  pin: str
  

class Patient(BaseModel):
  
  name: str
  gender: str ='Male'
  age: str
  address: Address
  
address_dict = {'city': 'Tezpur', 'state': 'Assam', 'pin': '784028'}

address1 = Address(**address_dict)

patient_dict = {'name':'Bhargab','age':'20','address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(exclude_unset=True)     #converts it into dictionary

print(temp)
print(type(temp))

temp1= patient1.model_dump_json()           #converts it into json format
print(temp1)
print(type(temp1))