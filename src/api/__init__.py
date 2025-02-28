import fastapi
from ..main import router
from fastapi.middleware.cors import CORSMiddleware

def create_app():

    app = fastapi.FastAPI (docs_url="/docs")
    origins = ["http://localhost:8000"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins = origins
    )
    
    app.include_router(router)
    return app