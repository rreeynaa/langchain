from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0
)

schema = {
    "title": "Books",
    "type": "object",
    "properties": {
        "books": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "author": {"type": "string"},
                    "year": {"type": "integer"}
                },
                "required": ["title", "author", "year"]
            }
        }
    },
    "required": ["books"]
}

structured_llm = llm.with_structured_output(schema)

response = structured_llm.invoke(
    """
    Recommend three books:
    1. Clean Code by Robert C. Martin (2008)
    2. Atomic Habits by James Clear (2018)
    3. Deep Learning by Ian Goodfellow (2016)
    """
)

print(response)