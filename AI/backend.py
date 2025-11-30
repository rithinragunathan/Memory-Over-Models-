from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from qdrant_client import QdrantClient
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Clients
qdrant_client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

COLLECTION_NAME = "hackathon_memory"

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    try:
        # 1. Retrieve
        search_result = qdrant_client.query(
            collection_name=COLLECTION_NAME,
            query_text=request.question,
            limit=3
        )
        
        context_str = "\n".join([r.metadata['document'] for r in search_result])
        sources = [r.metadata['document'] for r in search_result]

        # 2. Generate
        prompt = f"""
        Answer the user's question using ONLY the context provided below.
        Context: {context_str}
        Question: {request.question}
        """

        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )

        return {
            "answer": response.choices[0].message.content,
            "context": sources
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))