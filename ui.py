import streamlit as st
from core.orchestrator import run_system
from core.vectorstore import create_vectorstore

st.set_page_config(page_title="AI Research Agent", layout="centered")

# Header
st.title("🤖 Multi-Agent AI Research System")
st.markdown("🚀 Powered by Local AI + RAG + Multi-Agent Workflow")

# Initialize DB
create_vectorstore()

# Input box
query = st.text_input("💬 Ask your question:")

# Button
if st.button("Run AI"):
    if query:
        with st.spinner("🧠 Agents are thinking..."):
            result = run_system(query)

        st.success("✅ Answer Generated")

        st.markdown("### 📊 Final Result")
        st.write(result)
    else:
        st.warning("⚠️ Please enter a question")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | Multi-Agent AI System")
