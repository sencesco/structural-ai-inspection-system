from fastapi import APIRouter

router = APIRouter()


@router.post("/generate")
async def generate_report():
    return {"status": "placeholder", "report_id": None}

