import httpx
from fastapi import APIRouter

router = APIRouter(tags=["auth"])

@router.get("/callback")
async def callback(code: str, auth_service):
        tokens = await auth_service.authenticate(code)
        return tokens
