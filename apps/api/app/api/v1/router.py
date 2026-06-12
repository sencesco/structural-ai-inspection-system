from fastapi import APIRouter

from app.api.v1.routes import agent, health, inspect, inspections, models, report

api_router = APIRouter()
api_router.include_router(inspect.router, prefix="/inspect", tags=["inspect"])
api_router.include_router(report.router, prefix="/report", tags=["report"])
api_router.include_router(agent.router, prefix="/agent", tags=["agent"])
api_router.include_router(inspections.router, prefix="/inspections", tags=["inspections"])
api_router.include_router(models.router, prefix="/models", tags=["models"])
api_router.include_router(health.router, tags=["health"])

