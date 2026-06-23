from pydantic import BaseModel


class RepairPriorityRecommendation(BaseModel):
    status: str
    recommendation: str | None = None
