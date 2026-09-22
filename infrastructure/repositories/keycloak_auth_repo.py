from urllib.parse import urlencode

from domain.users import User
from interactors.interfaces.auth_repo_interface import AuthRepoInterface

class KeycloakAuthRepo(AuthRepoInterface):

    def __init__(self, keycloak_settings, http_client):
        self.keycloak_settings = keycloak_settings
        self.http_client = http_client

    async def code_to_tokens(self, code: str):
        response = await self.http_client.post(self.keycloak_settings.token_url,data={
            "grant_type": "authorization_code",
            "code": code,
            "client_id": self.keycloak_settings.keycloak_client_id,
            "client_secret": self.keycloak_settings.keycloak_client_secret,
            "redirect_uri": self.keycloak_settings.keycloak_redirect_uri,
        })

        return response.json()

    async def tokens_to_user(self, access_token: str):
        response = await self.http_client.get(self.keycloak_settings.user_info_url,
                                              headers={"Authorization": f"Bearer {access_token}"}
                                              )
        data = response.json()
        return User(username=data["preferred_username"], uuid=data["sub"])

    async def url_to_redirect(self):
        params = self.keycloak_settings.params_to_redirect
        return f"{self.keycloak_settings.authorization_url}?{urlencode(params)}"


