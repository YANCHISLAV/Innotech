import httpx
from fastapi import Depends

from configs.settings_manager import get_settings
from depends.depends_manager import get_http_client
from infrastructure.repositories.keycloak_auth_repo import KeycloakAuthRepo
from interactors.services.redirect_service import RedirectService


async def redirect_provider(http_client: httpx.AsyncClient = Depends(get_http_client))->RedirectService:

    keycloak_settings = get_settings().auth_settings
    auth_repo = KeycloakAuthRepo(keycloak_settings=keycloak_settings, http_client=http_client)
    return RedirectService(auth_repo=auth_repo)