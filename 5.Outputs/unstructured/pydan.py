from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="Age of the person")
    city: str = Field(description="Name of the city the person belongs to")

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.3
)

structured_model = model.with_structured_output(Person)

template = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person.",
    input_variables=["place"]
)

chain = template | structured_model

result = chain.invoke({"place": "Indian"})

print(result)
print(result.name)
print(result.age)
print(result.city)