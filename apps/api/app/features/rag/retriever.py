def retrieve(query: str) -> list[dict[str, str]]:
    return [{"query": query, "source": "placeholder"}] if query else []
