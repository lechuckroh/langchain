from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2-korean")

response = llm.invoke("GPT-4에 대해 설명해줘")
print(response)
