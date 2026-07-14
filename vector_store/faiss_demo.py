from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

documents = [
    "Virat Kohli is a batsman",
    "MS Dhoni is a wicketkeeper",
    "Jasprit Bumrah is a bowler"
]

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_texts(
    documents,
    embeddings
)

results = vectorstore.similarity_search_with_score(
    'Tell me about Dhoni',
    k=1
)
# print(results[0].page_content)

# for doc, score in results:
#     print(doc.page_content)
#     print(score)


vectorstore.save_local("faiss_index")