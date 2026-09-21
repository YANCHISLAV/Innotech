from pydantic import BaseModel

class AuthSettings(BaseModel):

    keycloak_base_url:str
    keycloak_realm: str
    keycloak_client_id: str
    keycloak_client_secret: str
    keycloak_redirect_uri: str

    def token_url(self):
        return f"{self.keycloak_base_url}/realms/{self.keycloak_realm}/protocol/openid-connect/token"

    def user_info_url(self):
        return f"{self.keycloak_base_url}/realms/{self.keycloak_realm}/protocol/openid-connect/userinfo"
