from fastapi import APIRouter

from app.features.rag import service

router = APIRouter()


@router.get("/guidelines")
async def retrieve_guidelines(query: str = ""):
    return service.retrieve_guidelines(query)
