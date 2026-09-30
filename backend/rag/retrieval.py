from backend.rag.embeddings import create_embeddings
from backend.rag.vector_store import search_documents


def retrieve_documents(query: str, top_k: int = 3):
    if not query:
        raise ValueError("Query is required.")

    query_embedding = create_embeddings([query])[0]

    results = search_documents(
        query_embedding=query_embedding,
        top_k=top_k
    )

    return results