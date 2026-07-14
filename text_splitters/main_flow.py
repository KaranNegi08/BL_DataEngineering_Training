from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


loader = TextLoader('cricket.txt')
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)
# print("Total Chunks: ", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\nChunk: {i+1}")
    print(chunk.page_content)