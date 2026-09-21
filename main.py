from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI

from configs.settings_manager import get_settings
from infrastructure.db.configs.session import DataBase


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    db = DataBase(
        **settings.db_settings.model_dump()
    )
    app.state.db = db
    async with httpx.AsyncClient() as client:
        app.state.http_client = client
        yield

    await db.dispose()
app = FastAPI(lifespan=lifespan)


