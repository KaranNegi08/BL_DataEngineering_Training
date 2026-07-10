from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-2.0-flash-001",
    google_api_key= os.getenv("GEMINI_API_KEY"),
    dimensions=30
)
vector = embeddings.embed_query("What is LangChain?")
print(str(vector))

# from google import genai
# import os

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# for model in client.models.list():
#     print(model.name)