import chromadb


COLLECTION_NAME = "customer_support_knowledge"


_client = chromadb.PersistentClient(
    path="data/chroma_db"
)


def get_collection():
    return _client.get_or_create_collection(
        name=COLLECTION_NAME
    )


def add_documents(chunks, embeddings):
    if len(chunks) != len(embeddings):
        raise ValueError(
            "The number of chunks must match the number of embeddings."
        )

    collection = get_collection()

    ids = [
        f"chunk_{index}"
        for index in range(len(chunks))
    ]

    documents = [
        chunk["content"]
        for chunk in chunks
    ]

    metadatas = [
        {
            "source": chunk["source"]
        }
        for chunk in chunks
    ]

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )

    return collection.count()


def search_documents(query_embedding, top_k=3):
    if not query_embedding:
        raise ValueError("Query embedding is required.")

    collection = get_collection()

    return collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )