from pydantic import BaseModel

class Address(BaseModel):
  
  city: str
  state: str
  pin: str
  

class Patient(BaseModel):
  
  name: str
  gender: str
  age: str
  address: Address
  
address_dict = {'city': 'Tezpur', 'state': 'Assam', 'pin': '784028'}

address1 = Address(**address_dict)

patient_dict = {'name':'Bhargab', 'gender':'Male','age':'20','address': address1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)
print(patient1.address.state)