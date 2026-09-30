from backend.rag.retrieval import retrieve_documents


def get_refund_policy():
    results = retrieve_documents(
        "What is the refund policy?",
        top_k=3
    )

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    if not documents:
        return {
            "success": False,
            "message": "Refund policy information was not found."
        }

    return {
        "success": True,
        "policy": documents[0],
        "source": metadatas[0].get(
            "source",
            "knowledge_base"
        )
    }