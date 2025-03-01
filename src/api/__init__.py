from fastapi import FastAPI
from ..main import router
from fastapi.middleware.cors import CORSMiddleware

def create_app() -> FastAPI:
    """
    Creates and configures an instance of the FastAPI application.

    Returns:
        FastAPI: An instance of the FastAPI application with CORS middleware and routes included.
    """
    app = FastAPI (docs_url="/docs")
    origins = ["http://localhost:8000"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins = origins
    )
    
    app.include_router(router)
    return app