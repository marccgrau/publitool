from typing import Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.post import Post
from app.models.user import User
from app.schemas.post import PostCreate, PostUpdate, PostUpdateImage, PostUpdateText

class CRUDPost(CRUDBase[Post, PostCreate, PostUpdate]):    
    def update(
        self,
        db: Session,
        *,
        db_obj: Post,
        obj_in: Union[PostUpdateImage, PostUpdateText]
    ) -> Post:
        db_obj = super().update(db, db_obj=db_obj, obj_in=obj_in)
        return db_obj

post = CRUDPost(Post)