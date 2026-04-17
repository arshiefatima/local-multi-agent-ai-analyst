import streamlit as st
from core.orchestrator import run_system
from core.vectorstore import create_vectorstore

st.set_page_config(page_title="AI Research Agent", layout="centered")

st.title("🤖 Local Multi-Agent AI System")
st.write("Ask questions based on your data")

# Initialize vector DB
create_vectorstore()

query = st.text_input("Enter your question:")

if st.button("Run AI"):
    if query:
        with st.spinner("Thinking..."):
            result = run_system(query)

        st.subheader("Result:")
        st.write(result)
    else:
        st.warning("Please enter a question.")