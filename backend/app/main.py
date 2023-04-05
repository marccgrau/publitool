from pathlib import Path

from fastapi import FastAPI, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.api.api_v1.api import api_router
from app.core.config import settings

BASE_PATH = Path(__file__).resolve().parent

root_router = APIRouter()
app = FastAPI(title="Publitool", openapi_url=f"{settings.API_V1_STR}/openapi.json")

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_origin_regex=settings.BACKEND_CORS_ORIGIN_REGEX,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@root_router.get("/", status_code=200)
def root(
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Root GET
    """
    user = crud.user.get(db=db, id=1)
    return {"user": user}


app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)


if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")