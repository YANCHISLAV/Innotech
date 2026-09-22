import httpx
from fastapi import Depends

from configs.settings_manager import get_settings
from depends.depends_manager import get_db, get_http_client
from infrastructure.db.configs.session import DataBase
from infrastructure.repositories.keycloak_auth_repo import KeycloakAuthRepo
from infrastructure.repositories.sqlalchemy_user_repo import SQLAlchemyUserRepo
from interactors.services.authenticate_service import AuthenticateService


async def auth_provider(db: DataBase = Depends(get_db),
                        http_client: httpx.AsyncClient = Depends(get_http_client)
                        ):

    keycloak_settings = get_settings().auth_settings
    async with db.session_factory() as session:
        try:
            user_repo = SQLAlchemyUserRepo(session=session)
            auth_repo = KeycloakAuthRepo(keycloak_settings=keycloak_settings, http_client=http_client)
            yield AuthenticateService(auth_repo=auth_repo, user_repo=user_repo)
            await session.commit()
        except Exception:
            await session.rollback()
            raise