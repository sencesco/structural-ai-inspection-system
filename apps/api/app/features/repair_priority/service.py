from app.features.repair_priority.schemas import RepairPriorityRecommendation


def recommend_priority() -> RepairPriorityRecommendation:
    return RepairPriorityRecommendation(status="placeholder")
