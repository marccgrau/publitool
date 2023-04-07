from sqlalchemy import String, Column, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from typing import List

from app.db.base_class import Base
from app.models.image import Image


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name = Column(String(256), nullable=True)
    surname = Column(String(256), nullable=True)
    email = Column(String, index=True, nullable=False)
    is_superuser = Column(Boolean, default=False)
    hashed_password = Column(String, nullable=False)
    images: Mapped[List["Image"]] = relationship()