import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="DocMind",
    page_icon="📄",
    layout="centered"
)

st.markdown("""
<style>
    /* Reset & Base */
    .stApp {
        background-color: #ffffff;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    .block-container {
        max-width: 760px;
        padding-top: 0rem;
    }

    /* Hide streamlit branding */
    #MainMenu, footer, header { visibility: hidden; }

    /* Navbar */
    .navbar {
        display: flex;
        width: 100%;
        justify-content: space-between;
        align-items: center;
        padding: 1.2rem 0 1.2rem 0;
        border-bottom: 1px solid #f0f0f0;
        margin-bottom: 0;
    }
    .navbar-brand {
        font-size: 1rem;
        font-weight: 700;
        color: #111;
        letter-spacing: -0.02em;
    }
    .navbar-links {
        display: flex;
        gap: 1.5rem;
    }
    .navbar-links a {
        color: #555;
        text-decoration: none;
        font-size: 0.9rem;
    }
    .navbar-btn {
        background: #111;
        color: white !important;
        padding: 0.4rem 1.1rem;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 500;
    }

    /* Hero */
    .hero {
        text-align: center;
        padding: 3rem 1rem 3rem 1rem;
    }
    .hero-icon {
        width: 64px;
        height: 64px;
        background: #111;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 1.5rem auto;
        font-size: 1.8rem;
        line-height: 64px;
        text-align: center;
    }
    .hero h1 {
        font-size: 3rem;
        font-weight: 800;
        color: #111;
        letter-spacing: -0.04em;
        line-height: 1.15;
        margin-bottom: 1rem;
    }
    .hero p {
        color: #777;
        font-size: 1rem;
        line-height: 1.6;
        max-width: 480px;
        margin: 0 auto 2rem auto;
    }

    /* Trust bar */
    .trust-bar {
        text-align: center;
        color: #aaa;
        font-size: 0.8rem;
        margin: 2rem 0 0.5rem 0;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }
    .trust-logos {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin: 0.5rem 0 3rem 0;
        flex-wrap: wrap;
    }
    .trust-logo {
        color: #ccc;
        font-size: 0.95rem;
        font-weight: 600;
        letter-spacing: -0.01em;
    }

    /* Section divider */
    .section-label {
        font-size: 0.75rem;
        font-weight: 600;
        color: #aaa;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 0.6rem;
    }

    /* Upload area */
    div[data-testid="stFileUploader"] {
        border: 1.5px dashed #ddd !important;
        border-radius: 12px !important;
        background: #fafafa !important;
        padding: 1rem !important;
    }
    div[data-testid="stFileUploader"]:hover {
        border-color: #aaa !important;
    }

    /* Input */
    .stTextInput input {
        border: 1.5px solid #e8e8e8 !important;
        border-radius: 0px !important;
        padding: 0.7rem 1.3rem !important;
        font-size: 0.95rem !important;
        color: #111 !important;
        background: #fff !important;
        box-shadow: none !important;
    }
    .stTextInput input:focus {
        border-color: #111;
    }
    .stTextInput input::placeholder {
        color: #bbb !important;
    }

    /* Buttons */
    .stButton button {
        background: #111 !important;
        color: white !important;
        border: none !important;
        border-radius: 50px !important;
        padding: 0.65rem 2rem !important;
        font-size: 0.9rem !important;
        font-weight: 600 !important;
        letter-spacing: -0.01em !important;
        transition: background 0.2s !important;
    }
    .stButton button:hover {
        background: #333 !important;
    }

    /* Answer box */
    .answer-box {
        background: #fafafa;
        border: 1.5px solid #ebebeb;
        border-radius: 16px;
        padding: 1.5rem 1.8rem;
        color: #222;
        font-size: 1rem;
        line-height: 1.75;
        margin-top: 1rem;
    }

    /* Source chips */
    .source-chip {
        background: #f5f5f5;
        border: 1px solid #ebebeb;
        border-radius: 10px;
        padding: 0.8rem 1rem;
        margin-bottom: 0.5rem;
        font-size: 0.82rem;
        color: #666;
        line-height: 1.5;
    }

    /* Steps */
    .step-row {
        display: flex;
        align-items: flex-start;
        gap: 1rem;
        margin-bottom: 1.5rem;
    }
    .step-num {
        background: #111;
        color: white;
        width: 26px;
        height: 26px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.75rem;
        font-weight: 700;
        flex-shrink: 0;
        margin-top: 2px;
    }
    .step-text {
        color: #444;
        font-size: 0.9rem;
        line-height: 1.5;
    }
    .step-title {
        font-weight: 600;
        color: #111;
    }

    /* Success / warning */
    .stSuccess {
        border-radius: 10px !important;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #ccc;
        font-size: 0.78rem;
        padding: 2rem 0 1rem 0;
        border-top: 1px solid #f0f0f0;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# --- Navbar ---
st.markdown("""
<div class="navbar">
    <div class="navbar-brand">⬛ DocMind</div>
    <div class="navbar-links">
        <a href="https://github.com/Saurabh89580/DocMind">GitHub</a>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Hero ---
st.markdown("""
<div class="hero">
    <div class="hero-icon">📄</div>
    <h1>Ask anything about<br>your documents.</h1>
    <p>Upload any PDF and get instant, accurate answers — powered by Gemini and RAG.</p>
</div>
""", unsafe_allow_html=True)

# --- Upload Section ---
st.markdown('<div class="section-label">Step 1 — Upload your PDF</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Drop your PDF here or click to browse",
    type="pdf",
    label_visibility="collapsed"
)

if uploaded_file:
    with st.spinner("Indexing document..."):
        response = requests.post(
            f"{API_URL}/upload",
            files={"file": (uploaded_file.name, uploaded_file, "application/pdf")}
        )
    if response.status_code == 200:
        data = response.json()
        st.success(f" {uploaded_file.name} indexed — {data['chunks_created']} chunks ready.")
        st.session_state["pdf_loaded"] = True
    else:
        st.error("Upload failed. Make sure the backend is running.")
        st.session_state["pdf_loaded"] = False

st.markdown("<br>", unsafe_allow_html=True)

# --- Query Section ---
st.markdown('<div class="section-label">Step 2 — Ask a question</div>', unsafe_allow_html=True)

col1, col2 = st.columns([4, 1])
with col1:
    question = st.text_input(
        "question",
        placeholder="What is this document about?",
        label_visibility="collapsed"
    )
with col2:
    ask_clicked = st.button("Ask →")

if ask_clicked and question:
    if not st.session_state.get("pdf_loaded"):
        st.warning("Please upload a PDF first.")
    else:
        with st.spinner(""):
            response = requests.post(
                f"{API_URL}/query",
                json={"question": question}
            )
        if response.status_code == 200:
            data = response.json()
            st.markdown(f'<div class="answer-box">{data["answer"]}</div>', unsafe_allow_html=True)
            if data.get("sources"):
                st.markdown("<br>", unsafe_allow_html=True)
                with st.expander("View source chunks"):
                    for i, source in enumerate(data["sources"]):
                        st.markdown(
                            f'<div class="source-chip"><b>#{i+1}</b> — {source}...</div>',
                            unsafe_allow_html=True
                        )
        else:
            st.error("Query failed. Try uploading the PDF again.")

# --- How it works ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown('<div class="section-label">How it works</div>', unsafe_allow_html=True)
st.markdown("""
<div style="margin-top: 1rem;">
    <div class="step-row">
        <div class="step-num">1</div>
        <div class="step-text"><span class="step-title">Upload a PDF.</span> Your document is split into chunks and embedded into a vector database.</div>
    </div>
    <div class="step-row">
        <div class="step-num">2</div>
        <div class="step-text"><span class="step-title">Ask a question.</span> Your query is matched against the most relevant chunks using semantic search.</div>
    </div>
    <div class="step-row">
        <div class="step-num">3</div>
        <div class="step-text"><span class="step-title">Get a grounded answer.</span> Gemini generates an answer using only the retrieved context — no hallucinations.</div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<div class="footer">
    DocMind · Built with FastAPI, LangChain, ChromaDB, Gemini & Streamlit
</div>
<div class="trust-bar">Powered by</div>
<div class="trust-logos">
    <span class="trust-logo">LangChain</span>
    <span class="trust-logo">ChromaDB</span>
    <span class="trust-logo">Gemini</span>
    <span class="trust-logo">FastAPI</span>
    <span class="trust-logo">Streamlit</span>
</div>
""", unsafe_allow_html=True)