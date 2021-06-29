from fastapi import FastApi

from starlette.middleware.cors import CORSMiddleware


def setup_cors(app: FastApi):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=False,
        expose_headers=[],
        max_age=600,
    )
