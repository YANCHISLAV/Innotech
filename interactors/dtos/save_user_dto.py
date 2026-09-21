from pydantic import BaseModel


class SaveUserDTO(BaseModel):
    uuid: str
    username: str