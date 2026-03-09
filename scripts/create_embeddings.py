import pandas as pd
from sentence_transformers import SentenceTransformer
import chromadb

df = pd.read_csv("data/lost_found_dataset.csv")

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(df["description"].tolist())

client = chromadb.Client()

collection = client.create_collection("lost_items")

collection.add(
    documents=df["description"].tolist(),
    embeddings=embeddings.tolist(),
    ids=df["id"].astype(str).tolist()
)

print("Embeddings stored in ChromaDB")
