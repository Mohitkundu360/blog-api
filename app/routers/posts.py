from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import List

from app import schemas
from app.models import Post, User
from app.database import get_db
from app.routers.auth import get_current_user

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

# --------- Create Post ---------
@router.post("/", response_model=schemas.PostOut)
def create_post(
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_post = Post(
        title=post.title,
        content=post.content,
        owner_id=current_user.id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# --------- Get All Posts (owned by current user only) ---------
@router.get("/", response_model=List[schemas.PostOut])
def get_all_posts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Post).filter(Post.owner_id == current_user.id).all()  # type: ignore

# --------- Get Single Post (if owned) ---------
@router.get("/{post_id}", response_model=schemas.PostOut)
def get_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    post = db.query(Post).filter(
        and_(Post.id == post_id, Post.owner_id == current_user.id)
    ).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


# --------- Delete Post ---------
@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    post = db.query(Post).filter(
        and_(Post.id == post_id, Post.owner_id == current_user.id)
    ).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    return None


# --------- Update Post ---------
@router.put("/{post_id}", response_model=schemas.PostOut)
def update_post(
    post_id: int,
    updated_post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    post = db.query(Post).filter(
        and_(Post.id == post_id, Post.owner_id == current_user.id)
    ).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    post.title = updated_post.title
    post.content = updated_post.content
    db.commit()
    db.refresh(post)
    return post
