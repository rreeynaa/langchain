from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.3
)

model2 = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.3
)

prompt1 = PromptTemplate(
    template="Generate 5 interesting facts about {topic}.",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate 5 questions on the topic {topic}.",
    input_variables=["topic"]
)

prompt3 = PromptTemplate(
    template="""
Merge the following into a single study document.

Facts:
{facts}

Questions:
{quiz}
""",
    input_variables=["facts", "quiz"]
)

parser = StrOutputParser()

facts_chain = prompt1 | model1 | parser
quiz_chain = prompt2 | model2 | parser

parallel_chain = RunnableParallel(
    facts=facts_chain,
    quiz=quiz_chain
)

chain = parallel_chain | prompt3 | model1 | parser

result = chain.invoke({"topic": "Unemployment"})

print(result)
#chain.get_graph().print_ascii() -> gives the chain working sequence as flowchart

"""
                 topic
                   │
          ┌────────┴────────┐
          │                 │
      prompt1           prompt2
          │                 │
       model1            model2
          │                 │
        parser           parser
          └────────┬────────┘
                   │
           RunnableParallel
                   │
               prompt3
                   │
                model1
                   │
                parser
                   │
                Output"""