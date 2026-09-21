from pydantic import BaseModel


class FindUserDTO(BaseModel):
    uuid: str
