from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_ACCESS_TOKEN")
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name:str = Field(description='Name of the person')
    age:int = Field(gt=18, description='Age of teh person')
    city:str = Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age,city of a fictional {place} person \n {format_instruction} \n IMPORTANT: Return ONLY a valid JSON object. Do not provide explanations. Do not provide code. Do not wrap in markdown.',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)

chain = template | model | parser
result = chain.invoke({'place':'american'})
print(result)
"""

splitter = RecursiveCharacterTextSplitter.from_language(
        language = Language.PYTHON,
        chunk_size = 200,
        chunk_overlap=0
)

chunks= splitter.split_text(text)
print(chunks[0])