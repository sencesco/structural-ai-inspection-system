from pydantic import BaseModel


class InferenceResult(BaseModel):
    status: str
    input_type: str
