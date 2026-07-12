from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
)

query = "What is Artificial Intelligence?"

embedding = embeddings.embed_query(query)

print("Dimension:", len(embedding))
print("First 10 values:")
print(embedding[:10])