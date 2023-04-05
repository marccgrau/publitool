from sqlalchemy_imageattach.entity import Image, image_attachment
from pydantic import BaseModel
from typing import Optional

class ImageBase(BaseModel):
    file_name: str
    content_type: str
    file_size: int

class ImageCreate(ImageBase):
    file_path: str

class Image(ImageBase):
    id: int
    post_id: int
    
    class Config:
        orm_mode = True
        
class ImageUpdate(Image):
    file_name: Optional[str]
    content_type: Optional[str]
    file_size: Optional[int]
    file_path: Optional[str]