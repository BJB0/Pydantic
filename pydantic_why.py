from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
  
  name: Annotated[str, Field(max_length=50,title='Name of the patient',description='Give the name of the patient in less than 50 characters',examples=['Bhargab','rohan'])]
  email:EmailStr
  linkedin_url: AnyUrl
  age: int = Field(gt=0, lt=110)
  weight: Annotated[float,Field(gt=0, strict=True)]
  married: Annotated[str,Field(default=None,description='is the patient married or not')]
  allergies: Annotated[Optional[list[str]],Field(default=None,max_length=5)]
  contact_details: Dict[str,str]



def insert_patient_data(patient: Patient):
  print(patient.name)
  print(patient.age)
  print('Inserted into Database')
  
def update_patient_data(patient: Patient):
  print(patient.name)
  print(patient.age)
  print(patient.allergies)
  print(patient.married)
  print('Updated')
  
  
  
patient_info = {'name': "Bhargab",'email':'bjbcr7@gmail.com','linkedin_url':'https://linkedin.com/bhargab-jb','age': 20, 'weight':82.4, 'contact_details':{'phn_no':'8822991076'}}

patient1 = Patient(**patient_info)


update_patient_data(patient1)
