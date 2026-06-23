from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Structural AI Inspection API"
    api_v1_prefix: str = "/api/v1"


settings = Settings()
