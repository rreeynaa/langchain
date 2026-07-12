#review passed to llm get sentiment and 
from typing import TypedDict,Annotated
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0
)
class Review(TypedDict):
    summary:Annotated[str,"A brief summary of the review"] #can guide llm by guiding it uysing annotated
    sentiment:str
structured_model=model.with_structured_output(Review)
result = structured_model.invoke(
    """The hardware is great, but the software feels bloated.
There are too many pre-installed apps that I can't remove. Also, the UI looks outdated
compared to other brands. Hoping for a software update to fix this."""
)
print(result)


