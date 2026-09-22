from interactors.dtos.find_user_dto import FindUserDTO
from interactors.dtos.save_user_dto import SaveUserDTO
from interactors.exceptions.auth_exception import AuthenticationFailed


class AuthenticateService:
    def __init__(self, auth_repo, user_repo):
        self.auth_repo = auth_repo
        self.user_repo = user_repo

    async def authenticate(self, code):
        if not code:
            raise AuthenticationFailed("Missing authorization code")
        tokens = await self.auth_repo.code_to_tokens(code)
        user = await self.auth_repo.tokens_to_user(tokens["access_token"])

        if not await self.user_repo.get(FindUserDTO(
            uuid=user.uuid,
        )):
            await self.user_repo.save(SaveUserDTO(
                uuid=user.uuid,
                username=user.username,
            ))
        return tokens
