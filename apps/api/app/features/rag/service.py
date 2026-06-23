from app.features.rag.retriever import retrieve


def retrieve_guidelines(query: str) -> dict[str, object]:
    return {"status": "placeholder", "results": retrieve(query)}
