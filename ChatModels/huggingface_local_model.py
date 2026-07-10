from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
import os

load_dotenv()
os.environ['HF_HOME']='D:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id = "microsoft/Phi-3-mini-4k-instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_ACCESS_TOKEN"),
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)
res= model.invoke("Greatest player of Test indian Cricket")
print(res.content)