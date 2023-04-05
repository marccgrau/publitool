from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session

from app import crud
from app import schemas
from app.api import deps
from app.models.user import User

from app.schemas.post import (
    Post,
    PostCreate,
    PostSearchResults,
    PostUpdateText,
    PostUpdateImage,
    )

router = APIRouter()


@router.get("/{post_id}", status_code=200, response_model=Post)
def fetch_post_by_id(
    *,
    post_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single post by ID
    """
    result = crud.post.get(db=db, id=post_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Post with ID {post_id} not found"
        )

    return result

@router.get("/my-posts/", status_code=200, response_model=PostSearchResults)
def fetch_user_posts(
    *,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> Any:
    """
    Fetch all recipes for a user
    """
    posts = current_user.posts
    if not posts:
        return {"results": list()}

    return {"results": list(posts)}

@router.post("/", response_model = Post, status_code=201)
def store_post(
    *,
    post_in: PostCreate,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> dict:
    """
    Store image and text in database.
    """
    if post_in.user_id != current_user.id:
        raise HTTPException(
            status_code=403, detail=f"You can only submit recipes as yourself"
        )
        
    post = crud.post.create(db=db, obj_in=post_in)

    return post

@router.put("/image", status_code=201, response_model=Post)
def update_post_image(
    *,
    data_in: PostUpdateImage,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> dict:
    """
    Update image of post in the database.
    """
    post = crud.post.get(db, id=data_in.id)
    if not post:
        raise HTTPException(
            status_code=400, detail=f"Post with ID: {data_in.id} not found."
        )

    if post.user_id != current_user.id:
        raise HTTPException(
            status_code=403, detail=f"You can only update your own posts."
        )

    updated_post = crud.post.update(db=db, db_obj=post, obj_in=data_in)
    return updated_post

@router.put("/text", status_code=201, response_model=Post)
def update_post_text(
    *,
    data_in: PostUpdateText,
    db: Session = Depends(deps.get_db),
    current_user: User = Depends(deps.get_current_user),
) -> dict:
    """
    Update image of post in the database.
    """
    post = crud.post.get(db, id=data_in.id)
    if not post:
        raise HTTPException(
            status_code=400, detail=f"Post with ID: {data_in.id} not found."
        )

    if post.user_id != current_user.id:
        raise HTTPException(
            status_code=403, detail=f"You can only update your own posts."
        )

    updated_post = crud.post.update(db=db, db_obj=post, obj_in=data_in)
    return updated_post

