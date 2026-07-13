from langchain_community.document_loaders import TextLoader

loader = TextLoader('cricket.txt',encoding='utf-8')

docs = loader.load()
# print(docs[0].metadata)
# print(docs[0].page_content)


from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")

)
model = llm



prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()
chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))