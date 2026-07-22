from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.7
)

# Create a Prompt Template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about {topic}."
)

# Define the input
topic = input("Enter a topic: ")

# Format the prompt
formatted_prompt = prompt.format(topic=topic)

# Call Gemini
response = llm.invoke(formatted_prompt)

# Print the output
print("Generated Blog Title:", response.content)