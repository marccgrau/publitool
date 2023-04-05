from sqlalchemy import Column, Integer, LargeBinary, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Post(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    image = Column(LargeBinary)
    text = Column(String)
    submitter_id = Column(Integer, ForeignKey('users.id'))
    submitter = relationship("User", back_populates="posts")
