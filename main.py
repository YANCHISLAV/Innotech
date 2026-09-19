from contextlib import asynccontextmanager

from fastapi import FastAPI

from configs.settings_manager import get_settings
from infrastructure.db.session import DataBase


@asynccontextmanager
async def lifespan(app: FastAPI):
    db = DataBase(
        **get_settings().db_settings.model_dump()
    )
    app.state.db = db

    yield

    await db.dispose()
app = FastAPI(lifespan=lifespan)


