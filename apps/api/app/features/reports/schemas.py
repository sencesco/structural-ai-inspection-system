from pydantic import BaseModel


class ReportResult(BaseModel):
    status: str
    report_id: str | None = None
