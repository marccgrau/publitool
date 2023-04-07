from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import mapped_column, Mapped

from app.db.base_class import Base


class Image(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    image_name = Column(String(256), nullable=True)
    image_url = Column(String(256), nullable=True)
    is_deleted = Column(Boolean, unique=False, default=False)
