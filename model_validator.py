# data validation combining multiple fields


from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
  
  name: str
  email: str
  age: int
  weight: float
  married: bool
  allergies: List[str]
  contact_details: Dict[str,str]
  
  @model_validator(mode='after')
  def validate_emergency_contact(cls, model):
    if model.age > 60 and "emergency" not in model.contact_details:
      raise ValueError('patients older than 60 must have an emergency contact')
    return model
      
    
      
      
    
  
  

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('Updated')
    
    
    
patient_info = {'name':'Bhargab', 'email':'bjbcr7@hdfc.com', 'age': '65', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'8822991076','emergency':'345678'}}


patient1 = Patient(**patient_info)

update_patient_data(patient1)