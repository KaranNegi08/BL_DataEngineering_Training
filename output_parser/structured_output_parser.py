from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
# from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_classic.output_parsers import (
    StructuredOutputParser,
    ResponseSchema
)
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_ACCESS_TOKEN")
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name = 'fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name = 'fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name = 'fact_3', description='Fact 3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)
template = PromptTemplate(
    template='Give 3 facts about  {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}

)

prompt = template.invoke({'topic':'black hole'})

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})
print(result)