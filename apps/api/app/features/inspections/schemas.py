from pydantic import BaseModel


class InspectionResult(BaseModel):
    status: str
    inspection_id: str
