#doc vs query and print scores enumerate scores and print sort ascending
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Query and document
query = "What is the capital of India?"
document = "New Delhi is the capital city of India."

# Generate embeddings
query_embedding = embeddings.embed_query(query)
document_embedding = embeddings.embed_query(document)

# Compute cosine similarity
similarity = cosine_similarity(
    [query_embedding],
    [document_embedding]
)

print("Cosine Similarity:", similarity[0][0])