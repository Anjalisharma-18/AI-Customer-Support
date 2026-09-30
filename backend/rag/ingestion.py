from pathlib import Path


KNOWLEDGE_BASE_PATH = Path("data/knowledge_base")


def load_documents():
    documents = []

    if not KNOWLEDGE_BASE_PATH.exists():
        raise FileNotFoundError(
            f"Knowledge base directory not found: {KNOWLEDGE_BASE_PATH}"
        )

    for file_path in sorted(KNOWLEDGE_BASE_PATH.glob("*.md")):
        content = file_path.read_text(encoding="utf-8").strip()

        if not content:
            continue

        documents.append({
            "source": file_path.name,
            "content": content
        })

    return documents