from fastapi import APIRouter

router = APIRouter()


@router.post("/image")
async def inspect_image():
    return {"status": "placeholder", "input_type": "image"}


@router.post("/video")
async def inspect_video():
    return {"status": "placeholder", "input_type": "video"}


@router.post("/sensor")
async def inspect_sensor():
    return {"status": "placeholder", "input_type": "sensor"}

