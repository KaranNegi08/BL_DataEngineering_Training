from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('testing.pdf')
docs= loader.load()

print(len(docs))
print(docs[2].page_content)