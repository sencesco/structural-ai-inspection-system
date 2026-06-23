from fastapi import APIRouter

from app.features.monitoring import service

router = APIRouter()


@router.get("/metrics")
async def get_model_metrics():
    return service.get_model_metrics()
