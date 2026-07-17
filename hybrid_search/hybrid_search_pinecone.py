from pinecone import Pinecone
from dotenv import load_dotenv
import os

load_dotenv()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

index = pc.Index("hybrid-index")

response = index.query(
    vector = dense_embeddings,
    sparse_vector ={
        "indices":sparse_indices,
        "value":sparse_values
    },
    top_k=5,
    include_metadata=True
)