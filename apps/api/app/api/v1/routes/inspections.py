from fastapi import APIRouter

router = APIRouter()


@router.get("/{inspection_id}")
async def get_inspection(inspection_id: str):
    return {"status": "placeholder", "inspection_id": inspection_id}

