from typing import Sequence

from pydantic import BaseModel

class PostBase(BaseModel):
    submitter_id: int
    image: bytes
    text: str

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    id: int

class PostUpdateText(BaseModel):
    id: int
    text: str

class PostUpdateImage(BaseModel):
    id: int
    image: bytes
    

# Properties shared by models stored in DB
class PostInDBBase(PostBase):
    id: int

    class Config:
        orm_mode = True

# Properties to return to client
class Post(PostInDBBase):
    pass


# Properties properties stored in DB
class PostInDB(PostInDBBase):
    pass


class PostSearchResults(BaseModel):
    results: Sequence[Post]
