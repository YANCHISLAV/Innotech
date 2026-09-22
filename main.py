from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI
from starlette.responses import JSONResponse

from configs.settings_manager import get_settings
from infrastructure.db.configs.session import DataBase
from interactors.exceptions.auth_exception import AuthenticationFailed
from interface_adapters import auth_view


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

app.include_router(auth_view.router)


@app.exception_handler(AuthenticationFailed)
async def auth_handler(request, exc):
    return JSONResponse(status_code=401, content={"detail": str(exc)})

