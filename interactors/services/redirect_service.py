

class RedirectService:
    def __init__(self, auth_repo):
        self.auth_repo = auth_repo

    async def redirect(self):
        return await self.auth_repo.url_to_redirect()