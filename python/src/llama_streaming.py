from langchain.schema import HumanMessage
from langchain_ollama import ChatOllama

chat = ChatOllama(model="llama3.2-korean")

for chunks in chat.stream([HumanMessage(content="맛있는 스테이크 굽는 법을 알려주세요!")]):
    print(chunks.content, end="", flush=True)
