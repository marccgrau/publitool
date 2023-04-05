from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, Optional

from app import crud
from app.api import deps
from app.schemas.user import User, UserCreate, UserUpdate

router = APIRouter()


@router.get("/{user_id}", status_code=200, response_model=User)
def fetch_user(
    *,
    user_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single recipe by ID
    """
    result = crud.user.get(db=db, id=user_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Recipe with ID {user_id} not found"
        )

    return result



@router.post("/", status_code=201, response_model=User)
def create_user(
    *, user_in: UserCreate, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new user in the database.
    """
    user = crud.user.create(db=db, obj_in=user_in)

    return user