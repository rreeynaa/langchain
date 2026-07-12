#outdated method not used now -> refer chatmodels for current use
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv() #to load .env file

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)

response = llm.invoke("hey") #invoke gives prompt to model

print(response.text)
#llms take string as input and give string as ouput