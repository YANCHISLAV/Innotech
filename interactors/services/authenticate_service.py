from interactors.dtos.user_dto import UserDTO


class AuthenticateService:
    def __init__(self, auth_repo, user_repo):
        self.auth_repo = auth_repo
        self.user_repo = user_repo

    async def authenticate(self, client, code):

        tokens = await self.auth_repo.code_to_token(client, code)
        if tokens is None:
            raise Exception('Authentication failed')
        user = UserDTO(
            **await self.user_repo.tokens_to_user(tokens)
        )
        if not user:
            await self.user_repo.save(user)
        return tokens
