from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser #used in chains usually

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.3
)
#prompt1-> detailed report
template1= PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

#prompt2->summarize
template2 = PromptTemplate(
    template='Write a 5line summary on the following {text}',
    input_variables=['text']
)
parser=StrOutputParser()
chain=template1 | model | parser | template2 | model | parser
result=chain.invoke({'topic':'blackhole'})
print(result)