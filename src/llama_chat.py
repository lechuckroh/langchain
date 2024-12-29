from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

chat = ChatOllama(model="llama3.2-korean")

prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
])

chain = prompt | chat

ai_msg = chain.invoke({
    "input": "iPhone14 출시일을 알려줘",
})
print(ai_msg.content)
