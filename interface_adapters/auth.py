import httpx
from fastapi import APIRouter

router = APIRouter(tags=["auth"])

@router.get("/callback")
async def callback(code: str, http_client: httpx.AsyncClient, auth_service):
        tokens = auth_service.authenticate(http_client, code)
        return tokens