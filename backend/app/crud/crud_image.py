from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.user import User
from app.schemas.image import Image, ImageCreate, ImageUpdate

class CRUDImage(CRUDBase[Image, ImageCreate, ImageUpdate]):    
    def update(
        self,
        db: Session,
        *,
        db_obj: Image,
        obj_in: ImageUpdate
    ) -> Image:
        db_obj = super().update(db, db_obj=db_obj, obj_in=obj_in)
        return db_obj

image = CRUDImage(Image)