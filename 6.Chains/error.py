from typing import Literal

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.runnables import RunnableBranch
from pydantic import BaseModel

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.3
)

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"]

parser = PydanticOutputParser(pydantic_object=Feedback)

classifier_prompt = PromptTemplate(
    template="""
Classify the sentiment of the following feedback as either positive or negative.

{format_instructions}

Feedback: {feedback}
""",
    input_variables=["feedback"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

positive_prompt = PromptTemplate.from_template(
    "Write a polite thank you reply to this feedback:\n{feedback}"
)

negative_prompt = PromptTemplate.from_template(
    "Write a polite apology and resolution for this feedback:\n{feedback}"
)

classifier = classifier_prompt | model | parser

positive_chain = positive_prompt | model | StrOutputParser()
negative_chain = negative_prompt | model | StrOutputParser()

branch = RunnableBranch(
    (
        lambda x: x["sentiment"].sentiment == "positive",
        positive_chain,
    ),
    negative_chain,
)

chain = classifier | branch

result = chain.invoke({"feedback": "This is terrible."})

print(result)