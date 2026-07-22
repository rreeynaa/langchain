from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
prompt=PromptTemplate(
    template='generate 5 interesting facts baout {topic}',
    input_variables=['topic']
)
model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.3
)
parser=StrOutputParser()
loader=TextLoader('cyber.txt',encoding='utf-8')
docs=loader.load()   #will load txt file as document
print(docs) #returns list
#docs will have all the docs loaded so when to access certain specifically docs[0]...

chain=prompt|model|parser
res=chain.invoke({'topic':docs[0].page_content})
print(res)