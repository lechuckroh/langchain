from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2-korean")

response = llm.invoke("iPhone14 출시일을 알려줘")
print(response)
