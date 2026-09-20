from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    uuid: str
    username: str

    model_config = ConfigDict(
        from_attributes=True
    )
