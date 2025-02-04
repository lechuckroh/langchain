import time

from langchain.globals import set_llm_cache
from langchain.schema import HumanMessage
from langchain_core.caches import InMemoryCache
from langchain_ollama import ChatOllama

set_llm_cache(InMemoryCache())

chat = ChatOllama(model="llama3.2-korean")

start = time.time()
result = chat.invoke([HumanMessage(content="안녕하세요!")])
end = time.time()
print(result.content)
print(f"Elapsed time: {end - start}s")

start = time.time()
result = chat.invoke([HumanMessage(content="안녕하세요!")])
end = time.time()
print(result.content)
print(f"Elapsed time: {end - start}s")
