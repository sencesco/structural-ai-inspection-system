from app.features.inference.schemas import InferenceResult


def inspect_input(input_type: str) -> InferenceResult:
    return InferenceResult(status="placeholder", input_type=input_type)
