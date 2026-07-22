from langchain_text_splitters import CharacterTextSplitter

text = """
Artificial Intelligence (AI) is transforming the way we live and work.
It is being used in healthcare, education, finance, transportation,
and many other industries. AI systems can analyze large amounts of
data, recognize patterns, and make predictions with remarkable accuracy.

Machine learning, a subset of AI, enables computers to improve their
performance through experience without being explicitly programmed.
Deep learning, which uses artificial neural networks, has led to major
advancements in computer vision, natural language processing, and speech
recognition.

Today, AI powers virtual assistants, recommendation systems, autonomous
vehicles, fraud detection, and even certain medical imaging techniques
trace their roots back to innovations developed for space programs.
"""

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=""
)

result = splitter.split_text(text)

print(result)

#text structure based - import RecursiveCharacterTextSplitter