from fastapi import APIRouter

from app.features.inspections import service

router = APIRouter()


@router.get("/{inspection_id}")
async def get_inspection(inspection_id: str):
    return service.get_inspection(inspection_id)
