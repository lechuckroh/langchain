from langchain.output_parsers import DatetimeOutputParser
from langchain.schema import HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

output_parser = DatetimeOutputParser(format="%Y-%m-%d")
chat = ChatOllama(model="llama3.2-korean")

prompt = PromptTemplate.from_template("{product}의 출시일을 알려주세요.")
result = chat.invoke([
    HumanMessage(content=prompt.format(product="iPhone8")),
    HumanMessage(content=output_parser.get_format_instructions()),
])

output = output_parser.parse(result.content)
print(output)