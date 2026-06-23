"""Placeholder for API and model-serving metrics."""


def record_metric(name: str, value: float, labels: dict[str, str] | None = None) -> None:
    """Record a metric value when Prometheus or another backend is wired in."""
    _ = (name, value, labels)
