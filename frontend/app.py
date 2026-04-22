import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(page_title="DocMind", page_icon="📄")
st.title("📄 DocMind – Document Q&A")
st.caption("Upload a PDF and ask questions about it")

# --- Upload Section ---
st.subheader("Step 1: Upload your PDF")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    with st.spinner("Ingesting document..."):
        response = requests.post(
            f"{API_URL}/upload",
            files={"file": (uploaded_file.name, uploaded_file, "application/pdf")}
        )
    if response.status_code == 200:
        data = response.json()
        st.success(f"✅ Ingested! {data['chunks_created']} chunks created.")
    else:
        st.error("Upload failed. Make sure the backend is running.")

# --- Query Section ---
st.subheader("Step 2: Ask a Question")
question = st.text_input("Enter your question about the document")

if st.button("Ask") and question:
    with st.spinner("Thinking..."):
        response = requests.post(
            f"{API_URL}/query",
            json={"question": question}
        )
    if response.status_code == 200:
        data = response.json()
        st.markdown("### 💬 Answer")
        st.write(data["answer"])

        with st.expander("📚 Source Chunks Used"):
            for i, source in enumerate(data["sources"]):
                st.markdown(f"**Chunk {i+1}:** {source}...")
    else:
        st.error("Query failed. Make sure you uploaded a PDF first.")