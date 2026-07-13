from langchain_community.document_loaders import WebBaseLoader

url="https://www.amazon.in/Casio-Edifice-EFB-730D-2BVUDF-Analog-ED688/dp/B0G1BY57RV/ref=sr_1_2_sspa?crid=DI77Y49XEJX2&dib=eyJ2IjoiMSJ9.dmUmETWbDkQeh9U6SSjgSvAPO14_3bMTJ8gVVzFOLehjhdghzbH2HwcErGey2qhNiaOfBVbDAKi9PqXRMNS_nXtlvCEoYz0fDAmSxvU1zYocNI6GupuELBvAlCuOdFLTWQvifTZh2EfB_c2kWcxVJErY8QV9WeZdKv1VlQRUto2ZqvXnC_Mc1WKOfAM6hbP7Bd5QXg2KAtAyTQbsP7RfVjxEnCEZdgWfzurygMaNhy3zIrmAvDe4PTjg1YGI6Q2n0kegMxptHD_2Ydpl34bUhjfjY-ax-pX9zTS8OEJ-ars.DbBaP-yRngx91nf_M6Dl5BG7JTgzOXPjDe98ns5HGTg&dib_tag=se&keywords=casio+watch+for+man&qid=1783963845&sprefix=casio%2Caps%2C415&sr=8-2-spons&aref=crp27V2D85&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
loader = WebBaseLoader(url)
docs = loader.load()

# print(docs[0].page_content)
print(len(docs))