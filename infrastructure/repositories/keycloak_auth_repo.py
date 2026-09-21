from domain.users import User
from interactors.interfaces.auth_repo_interface import AuthRepoInterface

class KeycloakAuthRepo(AuthRepoInterface):

    def __init__(self, keycloak_settings, http_client):
        self.keycloak_settings = keycloak_settings
        self.http_client = http_client

    async def code_to_tokens(self, code: str):
        response = await self.http_client.post(self.keycloak_settings.token_url(),data={
            "grant_type": "authorization_code",
            "code": code,
            "client_id": self.keycloak_settings.keycloak_client_id,
            "client_secret": self.keycloak_settings.keycloak_client_secret,
            "redirect_uri": self.keycloak_settings.keycloak_redirect_uri,
        })
        response.raise_for_status()
        return response.json()

    async def tokens_to_user(self, access_token: str):
        response = await self.http_client.get(self.keycloak_settings.user_info_url(),
                                              headers={"Authorization": f"Bearer {access_token}"}
                                              )
        response.raise_for_status()
        data = response.json()
        return User(username=data["name"], uuid=data["sub"])
