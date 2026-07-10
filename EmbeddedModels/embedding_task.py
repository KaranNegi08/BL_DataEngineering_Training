from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents=[
"Virat Kohli is an Indian cricketer. He is a right-handed batsman and one of the highest run scorers in international cricket.",
"Rohit Sharma is an Indian cricketer. He is a right-handed batsman and has captained India in multiple formats.",
"MS Dhoni is an Indian wicketkeeper-batsman. He captained India to victory in the 2011 Cricket World Cup.",
"Jasprit Bumrah is an Indian fast bowler. He is famous for his yorkers and exceptional death-over bowling.",
"Hardik Pandya is an Indian all-rounder. He contributes with both bat and ball in limited-overs cricket."
]

query= "tell me about Pandya"

doc_embeddings = embeddings.embed_documents(documents)
query_embeddings = embeddings.embed_query(query)

scores = cosine_similarity([query_embeddings],doc_embeddings)[0]
index, score = sorted(list(enumerate(scores)), key= lambda x:x[1])[-1]
print(documents[index])
print("Similarity score is: ", score)

