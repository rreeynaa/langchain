from typing import TypedDict
class Person(TypedDict):
    name:str
    age:int
person1:Person={"name":"reyna","age":35}
print(person1)