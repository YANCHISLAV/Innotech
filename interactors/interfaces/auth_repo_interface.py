from abc import ABC, abstractmethod

class AuthRepoInterface(ABC):

    @abstractmethod
    async def code_to_tokens(self, client, code):
        pass

    @abstractmethod
    async def tokens_to_user(self):
        pass