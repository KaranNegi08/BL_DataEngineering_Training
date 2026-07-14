from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader("testing2.pdf")
docs = loader.load()

splitter = CharacterTextSplitter(
    separator="",
    chunk_size=60,
    chunk_overlap=10 #overlapping characters between two chunks 
)

chunks = splitter.split_documents(docs)
print(chunks[0].page_content)