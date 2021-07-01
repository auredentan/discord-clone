from fastapi import FastApi

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

def setup_tracing(app: FastApi):
    FastAPIInstrumentor.instrument_app(app)
