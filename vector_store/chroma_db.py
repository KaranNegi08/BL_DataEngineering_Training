from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "Virat Kohli is a batsman",
    "MS Dhoni is a wicketkeeper",
    "Jasprit Bumrah is a bowler"
]

vectorstore = Chroma.from_texts(
    documents,
    embeddings,
    persist_directory="./chroma_db"
)

results = vectorstore.similarity_search(
    "Who is Bumrah?",
    k=1
)

# print(results[0].page_content)
# print(vectorstore.get(include=['embeddings','documents'])) 
print(vectorstore.similarity_search_with_score(
    'Who among these are a bowler',
    k=2
))