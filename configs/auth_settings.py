from pydantic import BaseModel

class AuthSettings(BaseModel):

    keycloak_base_url:str
    keycloak_realm: str
    keycloak_client_id: str
    keycloak_client_secret: str
    keycloak_redirect_uri: str

