from fastapi import APIRouter

from app.features.repair_priority import service

router = APIRouter()


@router.post("/recommend")
async def recommend_repair_priority():
    return service.recommend_priority()
