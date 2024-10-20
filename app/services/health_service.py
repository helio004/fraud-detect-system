from fastapi import APIRouter
from pydantic import BaseModel


health_router = APIRouter(
    prefix="/health",
    tags=["health-service"],
)


@health_router.get(path='.')
async def health():
    return {"status": "UP"}
