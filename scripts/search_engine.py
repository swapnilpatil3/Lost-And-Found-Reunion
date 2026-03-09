from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()

collection = client.get_collection("lost_items")

def search_items(query):

    query_embedding = model.encode([query])

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=5
    )

    return results
