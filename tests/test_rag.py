from backend.rag.retrieval import retrieve_documents


def test_rag_retrieval():
    results = retrieve_documents(
        "What is the standard delivery time?",
        top_k=3
    )

    assert "documents" in results
    assert "metadatas" in results

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    assert len(documents) > 0
    assert len(metadatas) > 0

    sources = [
        metadata.get("source")
        for metadata in metadatas
    ]

    assert any(
        source in ["shipping_policy.md", "faq.md"]
        for source in sources
    )