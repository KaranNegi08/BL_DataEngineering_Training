from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2,
    max_completion_tokens=20,
    api_key=os.getenv("OPENAI_KEY")
)
response = llm.invoke("Todays weather in Agra?")
print(response.content)

 