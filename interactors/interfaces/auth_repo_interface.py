from abc import ABC, abstractmethod


class AuthRepoInterface(ABC):

    @abstractmethod
    async def code_to_tokens(self, code):
        pass

    @abstractmethod
    async def tokens_to_user(self, access_token: str):
        pass

    @abstractmethod
    async def url_to_redirect(self) -> str:
        pass
