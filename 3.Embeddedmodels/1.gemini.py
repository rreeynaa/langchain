from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

vector = embeddings.embed_query("What is LangChain?")

print(len(vector))
print(vector[:5])  # First 5 values