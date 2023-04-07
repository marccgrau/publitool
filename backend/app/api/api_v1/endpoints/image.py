import boto3
from typing import List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm.session import Session

from app import crud
from app import schemas
from app.api import deps
from app.models.user import User

router = APIRouter()

@router.get("/{id}", response_model=schemas.Image)
def fetch_image(image_id: int, db: Session = Depends(deps.get_db)):
    return crud.image.get(db=db, id=image_id)