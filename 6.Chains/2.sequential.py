from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.3
)
prompt1=PromptTemplate(
    template='generate 5 interesting facts baout {topic}',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='generate 5 pointer summary from the following {text}',
    input_variables=['text']
)
parser=StrOutputParser()
chain=prompt1| model | parser| prompt2 | model | parser
res=chain.invoke({'topic':'unemployment'})
print(res)