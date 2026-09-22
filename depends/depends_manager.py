import httpx
from fastapi import Request

from infrastructure.db.configs.session import DataBase


def get_db(request: Request)->DataBase:
    return request.app.state.db

def get_http_client(request: Request)->httpx.AsyncClient:
    return request.app.state.http_client
