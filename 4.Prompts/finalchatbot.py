#have to do chat prompt template and message holder last part of video
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0.3
)

print("AI Chatbot")
print("Type 'exit' to end the chat.\n")
chat_history = [
    SystemMessage(content="You are a helpful AI assistant")
]
#we need to add chat history to be contxt aware and labels to know if human system or ai message
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=user_input))
    result = model.invoke(chat_history)
    ai_response = result.content[0]["text"]
    print("AI:", ai_response)
    chat_history.append(AIMessage(content=ai_response))

print("\nChat History:")
print(chat_history)
