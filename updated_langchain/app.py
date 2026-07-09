from dotenv import load_dotenv
load_dotenv()

# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# llm = ChatOpenAI(
#     model="llama-3.1-8b-instant",
#     base_url="https://api.groq.com/openai/v1",
#     api_key=os.getenv("OPENAI_KEY")
# )

gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    api_key = os.getenv("GEMINI_API_KEY")
)

print(gemini_llm.invoke("Where is GLA University?"))
