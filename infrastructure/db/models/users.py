from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from infrastructure.db.models.base import Base


class UserModel(Base):
    __tablename__ = 'users'
    uuid: Mapped[str] = mapped_column(String(50), primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)