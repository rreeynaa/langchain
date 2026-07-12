#used for api design -> data validation and parsing tool
#pydantic capable of implicit typecasting and can validate email 
from pydantic import BaseModel
class Student(BaseModel):
    name:str
new_student={'name':'reyna'} #if integer passed gives error
student=Student(**new_student)
print(student)