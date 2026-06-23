from fastapi import APIRouter

from app.api.v1 import health
from app.features.inference.router import router as inference_router
from app.features.inspections.router import router as inspections_router
from app.features.monitoring.router import router as monitoring_router
from app.features.rag.router import router as rag_router
from app.features.repair_priority.router import router as repair_priority_router
from app.features.reports.router import router as reports_router

api_router = APIRouter()
api_router.include_router(inference_router, prefix="/inspect", tags=["inference"])
api_router.include_router(reports_router, prefix="/reports", tags=["reports"])
api_router.include_router(repair_priority_router, prefix="/repair-priority", tags=["repair-priority"])
api_router.include_router(inspections_router, prefix="/inspections", tags=["inspections"])
api_router.include_router(rag_router, prefix="/rag", tags=["rag"])
api_router.include_router(monitoring_router, prefix="/monitoring", tags=["monitoring"])
api_router.include_router(health.router, tags=["health"])
