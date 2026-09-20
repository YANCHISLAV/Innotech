from interactors.interfaces.auth_repo_interface import AuthRepoInterface

class KeycloakAuthRepo(AuthRepoInterface):

    async def code_to_tokens(self, http_client, code):
        pass

    async def tokens_to_user(self):
        pass
