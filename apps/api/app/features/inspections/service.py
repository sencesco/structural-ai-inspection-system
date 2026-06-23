from app.features.inspections.schemas import InspectionResult


def get_inspection(inspection_id: str) -> InspectionResult:
    return InspectionResult(status="placeholder", inspection_id=inspection_id)
