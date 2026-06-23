from fastapi import APIRouter

from app.features.reports import service

router = APIRouter()


@router.post("/generate")
async def generate_report():
    return service.generate_report()
