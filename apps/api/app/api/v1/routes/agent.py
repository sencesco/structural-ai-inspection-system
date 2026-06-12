from fastapi import APIRouter

router = APIRouter()


@router.post("/recommend")
async def recommend_repair_priority():
    return {"status": "placeholder", "recommendation": None}

