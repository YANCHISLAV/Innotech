from abc import ABC, abstractmethod

class UserRepoInterface(ABC):

    @abstractmethod
    async def get(self, user):
        pass

    @abstractmethod
    async def save(self, user):
        pass