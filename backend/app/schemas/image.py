from pydantic import BaseModel
from typing import Optional

class ImageBase(BaseModel):
    image_name: str
    image_url: str
    is_deleted: bool

class ImageCreate(ImageBase):
    pass

class Image(ImageBase):
    id: Optional[int]
    user_id: Optional[int]
    
    class Config:
        orm_mode = True
        
class ImageUpdate(Image):
    image_name: Optional[str]
    image_url: Optional[str]
    is_deleted: Optional[bool]