# ai-fintech-rag-advisor

# AI FinTech RAG Advisor

End-to-end Retrieval Augmented Generation (RAG) system for financial advisory use cases.
Designed to convert unstructured financial documents into grounded, explainable AI responses.

## Problem
Financial advisors spend hours manually reviewing reports, disclosures, and portfolio documents.

## Solution
An AI-powered RAG system that:
- Retrieves relevant financial context using vector embeddings
- Generates grounded responses using LLMs
- Ensures explainability and reduced hallucinations

## Tech Stack
- Python
- OpenAI / Hugging Face
- LangChain
- FAISS / ChromaDB
- FastAPI
- Streamlit

## Architecture
Documents → Chunking → Embeddings → Vector DB  
User Query → Similarity Search → Prompt Chain → LLM → Response

## Key Features
- Prompt chaining with financial guardrails
- Embedding-based retrieval
- API-based deployment
- UI for live demos

## How to Run
```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
