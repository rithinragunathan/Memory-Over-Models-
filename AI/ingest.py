import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient, models
from qdrant_client.http.models import Distance, VectorParams

# Load keys
load_dotenv()

# Setup Client
qdrant_client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

COLLECTION_NAME = "hackathon_memory"

# 1. Create Collection
if not qdrant_client.collection_exists(COLLECTION_NAME):
    qdrant_client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )
    print(f"Created collection: {COLLECTION_NAME}")

# 2. Add Data (Example Data - Replace with your PDF parsing logic)
documents = [
    "Hackathon Theme 1: Unstructured Data RAG Challenge. Convert messy PDFs into retrieval systems.",
    "Hackathon Theme 2: AI Second Brain. Build a persistent memory OS for notes and tasks.",
    "Hackathon Theme 3: Domain-Specific AI Systems. Build retrieval for health, finance, law.",
    "Submission Deadline: November 30, 2025, 12 PM IST.",
    "The hackathon requires using Qdrant as the vector database.",
    "Pure chatbot UIs are NOT allowed. You must build a functional dashboard or tool.",
    "Prizes include 10,000 INR cash for top 3 and GCP credits for top 20."
]

metadata = [{"source": "guide_v1.pdf"} for _ in documents]

print("Uploading vectors...")
qdrant_client.add(
    collection_name=COLLECTION_NAME,
    documents=documents,
    metadata=metadata,
    ids=range(len(documents))
)
print("Success! Data ingested.")