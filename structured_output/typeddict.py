from typing import TypedDict

# class Person(TypedDict):
#     name:str
#     age:int

# new_person : Person={'name':'kk bhai','age':20}

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_ACCESS_TOKEN")
)

model = ChatHuggingFace(llm=llm)

#SCHEMA
class Review(TypedDict):
    summary:str
    sentiment:str

structured_model = model.with_structured_output(Review)
# result = structured_model.invoke("""
# The hardware is great, but the software feels bloated. There are too many pre-installed apps
# that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.
# """)

# print(result)

try:
    result = structured_model.invoke("""
    The hardware is great, but the software feels bloated. There are too many pre-installed apps
    that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.
    """)
    print(result)
except Exception as e:
    print(e)


