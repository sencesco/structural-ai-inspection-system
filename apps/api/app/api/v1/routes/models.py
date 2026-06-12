from fastapi import APIRouter

router = APIRouter()


@router.get("/metrics")
async def get_model_metrics():
    return {"status": "placeholder", "metrics": {}}

