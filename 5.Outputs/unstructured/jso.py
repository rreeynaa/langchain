from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser #used in chains usually

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.3
)

parser=JsonOutputParser()
template = PromptTemplate(
    template='Give me the name, age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={
        'format_instruction': parser.get_format_instructions()
    }
)
prompt=template.format()
print(prompt)
result=model.invoke(prompt)
print(result)
finalres=parser.parse(result.content)
print(finalres)
