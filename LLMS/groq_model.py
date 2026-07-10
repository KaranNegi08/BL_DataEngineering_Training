from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(api_key="OPENAI_API_KEY")

response = llm.invoke("What is LangChain?")
print(response)