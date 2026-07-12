#variable inserted into predefined templates 
#chose over since default validation,reusable(json file),langchain ecosystem
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import streamlit as st

# Load environment variables
load_dotenv()

# Create Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0.3
)

# Streamlit UI
st.set_page_config(page_title="Research Tool", page_icon="📚")

st.title("📚 Research Paper Summarizer")

# Select Paper
paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

# Select Style
style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

# Select Length
length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (Detailed Explanation)"
    ]
)

# Prompt Template
prompt_template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications.

Explanation Style: {style_input}

Explanation Length: {length_input}

1. Mathematical Details
- Include relevant mathematical equations if present in the paper.
- Explain the mathematical concepts using simple, intuitive code snippets wherever applicable.

2. Analogies
- Use relatable analogies to simplify complex ideas.

If certain information is not available in the paper, respond with "Insufficient information available" instead of guessing.

Ensure the summary is clear, accurate, and aligned with the selected explanation style and length.
""",
    input_variables=[
        "paper_input",
        "style_input",
        "length_input"
    ]
)

# Button
if st.button("Summarize"):

    prompt = prompt_template.invoke(
        {
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input
        }
    )

    with st.spinner("Generating summary..."):
        response = model.invoke(prompt)

    st.subheader("Summary")
    st.write(response.text)