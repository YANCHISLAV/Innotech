from fastapi import APIRouter, Depends
from starlette.responses import RedirectResponse

from depends.auth_provider import auth_provider
from depends.redirect_provider import redirect_provider
from interactors.exceptions.auth_exception import AuthenticationFailed
from interactors.services.authenticate_service import AuthenticateService
from interactors.services.redirect_service import RedirectService

router = APIRouter(tags=["auth"])


@router.get("/callback")
async def callback(
        code: str | None = None,
        error: str | None = None,
        auth_service: AuthenticateService = Depends(auth_provider),
):
        if error or not code:
            raise AuthenticationFailed(error or "Missing authorization code")
        await auth_service.authenticate(code)
        return RedirectResponse(url="/", status_code=302)


@router.get("/login")
async def login(auth_service: RedirectService = Depends(redirect_provider)):
    return RedirectResponse(await auth_service.redirect(), status_code=302)
