from fastapi import FastAPI  # type: ignore[attr-defined]

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor  # type: ignore[attr-defined]


def setup_tracing(app: FastAPI) -> None:
    FastAPIInstrumentor.instrument_app(app)
