from pydantic import BaseModel

class AuthSettings(BaseModel):

    keycloak_base_url:str
    keycloak_realm: str
    keycloak_client_id: str
    keycloak_client_secret: str
    keycloak_redirect_uri: str

    @property
    def authorization_url(self) -> str:
        return f"{self.keycloak_base_url}/realms/{self.keycloak_realm}/protocol/openid-connect/auth"

    @property
    def token_url(self):
        return f"{self.keycloak_base_url}/realms/{self.keycloak_realm}/protocol/openid-connect/token"

    @property
    def user_info_url(self):
        return f"{self.keycloak_base_url}/realms/{self.keycloak_realm}/protocol/openid-connect/userinfo"

    @property
    def params_to_redirect(self):
        return {
            "client_id": self.keycloak_client_id,
            "redirect_uri": self.keycloak_redirect_uri,
            "response_type": "code",
            "scope": "openid profile email",
        }