from fastapi import FastAPI  # type: ignore[attr-defined]

from starlette.middleware.cors import CORSMiddleware


def setup_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=False,
        expose_headers=[],
        max_age=600,
    )
