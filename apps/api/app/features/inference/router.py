from fastapi import APIRouter

from app.features.inference import service

router = APIRouter()


@router.post("/image")
async def inspect_image():
    return service.inspect_input("image")


@router.post("/video")
async def inspect_video():
    return service.inspect_input("video")


@router.post("/sensor")
async def inspect_sensor():
    return service.inspect_input("sensor")
