from langchain.output_parsers import PydanticOutputParser
from langchain.schema import HumanMessage
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field, field_validator

class Smartphone(BaseModel):
    release_date: str = Field(description="출시일")
    display_size: float = Field(description="디스플레이 크기(인치)")
    os: str = Field(description="OS")
    model_name: str = Field(description="모델명")

    @field_validator("display_size")
    def validate_screen_inches(cls, field):
        if field <= 0:
            raise ValueError("Display size must be a positive number")
        return field

chat = ChatOllama(model="llama3.2-korean")
parser = PydanticOutputParser(pydantic_object=Smartphone)
result = chat.invoke([
    HumanMessage(content="아이폰8의 출시일, 디스플레이 크기, OS, 모델명을 알려줘"),
    HumanMessage(content=parser.get_format_instructions()),
])
print(result)

try:
    parsed_result = parser.parse(result.content)
    print(f"모델명: {parsed_result.model_name}")
    print(f"디스플레이 크기: {parsed_result.display_size}인치")
    print(f"OS: {parsed_result.os}")
    print(f"출시일: {parsed_result.release_date}")
except Exception as e:
    print(f"파싱 에러: {e}")
    print("응답 원본: ", result.content)