from langchain_community.document_loaders import PyPDFLoader #used mostly for textual pdfs
loader=PyPDFLoader('document.pdf')
docs=loader.load()
print(len(docs))
