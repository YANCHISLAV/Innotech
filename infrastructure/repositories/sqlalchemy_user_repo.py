from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from domain.users import User
from infrastructure.db.models.users import UserModel
from interactors.interfaces.user_repo_interface import UserRepoInterface


class SQLAlchemyUserRepo(UserRepoInterface):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, user):
        query = select(UserModel).where(UserModel.uuid==user.uuid)
        query_response = await self.session.execute(query)
        user_model = query_response.scalar()
        if not user_model:
            return None
        return User.model_validate(user_model)

    async def save(self, user):
        user_model = UserModel(**user.model_dump())
        self.session.add(user_model)
        await self.session.flush()
        await self.session.refresh(user_model)
        await self.session.commit()
