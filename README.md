# DocMind – RAG-Powered Document Q&A

Ask questions about any PDF using AI.

## Tech Stack
- FastAPI (backend REST API)
- LangChain (RAG pipeline)
- ChromaDB (vector store)
- OpenAI GPT-3.5 (LLM)
- Streamlit (frontend UI)

## Architecture
PDF → Chunking → Embedding → ChromaDB → Retrieval → LLM → Answer

## Setup
1. Clone the repo
2. Add your OpenAI key to `.env`
3. `pip install -r backend/requirements.txt`
4. Run backend: `uvicorn main:app --reload`
5. Run frontend: `streamlit run frontend/app.py`