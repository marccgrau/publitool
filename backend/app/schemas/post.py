from typing import Sequence, List, Optional
import datetime
from pydantic import BaseModel

from app.schemas.post_image import Image, ImageCreate, ImageUpdate

class PostBase(BaseModel):
    text: str

class PostCreate(PostBase):
    user_id: int
    images: List[ImageCreate]

class PostInDBBase(PostBase):
    id: int
    created_at: datetime.datetime
    user_id: int
    images: List[Image]
    
    class Config:
        orm_mode = True


# Properties to return to client
class Post(PostInDBBase):
    pass


# Properties properties stored in DB
class PostInDB(PostInDBBase):
    pass

class PostUpdate(Post):
    text: Optional[str]
    images: Optional[List[ImageUpdate]]  


class PostSearchResults(BaseModel):
    results: Sequence[Post]
