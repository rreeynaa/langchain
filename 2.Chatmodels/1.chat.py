from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API key from .env
load_dotenv()

# Initialize Gemini Chat Model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=1.6
)

# Ask a question
response = llm.invoke("suggest 5 indian names")

# Print response
print(response.text)

#similarly can add another api key in env and create one more file to access