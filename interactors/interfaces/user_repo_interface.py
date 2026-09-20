from abc import ABC, abstractmethod

class UserRepoInterface(ABC):

    @abstractmethod
    async def get(self):
        pass

    @abstractmethod
    async def save(self):
        pass