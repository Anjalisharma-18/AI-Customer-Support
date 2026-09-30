def chunk_documents(documents, chunk_size=500, overlap=50):
    chunks = []

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0.")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be >= 0 and smaller than chunk_size.")

    for document in documents:
        content = document["content"]
        source = document["source"]

        start = 0

        while start < len(content):
            end = start + chunk_size
            chunk_text = content[start:end].strip()

            if chunk_text:
                chunks.append({
                    "source": source,
                    "content": chunk_text
                })

            if end >= len(content):
                break

            start = end - overlap

    return chunks