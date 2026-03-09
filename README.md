# Lost & Found Reunion

This project builds a semantic search engine that helps users find lost items using natural language queries.

## Problem

Traditional lost-and-found systems rely on manual searching through spreadsheets with vague descriptions. This makes it difficult to match lost items with found items.

## Solution

This project creates a semantic search engine using text embeddings and vector databases.

## Workflow

1. Dataset Creation
Generated 500 synthetic lost-item records using Python.

2. Data Processing
Used pandas to structure the dataset.

3. Embeddings
Used Sentence Transformers to convert item descriptions into vector embeddings.

4. Vector Database
Stored embeddings in ChromaDB for fast similarity search.

5. Semantic Search
User queries are embedded and compared with stored vectors.

6. User Interface
Streamlit UI allows users to search items easily.

## Tools Used

- Python
- Sentence Transformers
- ChromaDB
- Streamlit
- Pandas

## Future Improvements

- Add image search using CLIP
- Scrape real product data from Amazon/Flipkart
- Deploy using cloud infrastructure
