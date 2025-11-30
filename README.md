# Memory Over Models - Hackathon Entry

## Project Concept
This project is a Retrieval Augmented Generation (RAG) system built to answer questions about hackathon documentation. It uses **Qdrant** to store vector embeddings of the rulebook and allows users to query specific details like deadlines, themes, and prizes.

## Technologies Used
- **Vector Database:** Qdrant Cloud (Required) [cite: 16]
- **LLM:** OpenAI GPT-4o
- **Backend:** FastAPI (Python)
- **Frontend:** Streamlit
- **Embeddings:** FastEmbed (via Qdrant)

##  How We Used Qdrant 
We utilized Qdrant Cloud to store the text chunks of the resource guide. 
1. The text was embedded using the `fast-bge-small-en` model.
2. We used a Cosine distance metric for similarity search.
3. The `qdrant-client` python library manages the connection and vector retrieval.

## Setup Instructions 
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with `QDRANT_URL`, `QDRANT_API_KEY`, and `OPENAI_API_KEY`.
4. Run ingestion: `python ingest.py`
5. Start backend: `uvicorn backend:app --reload`
6. Start frontend: `streamlit run frontend.py`

