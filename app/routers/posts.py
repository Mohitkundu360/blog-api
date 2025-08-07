from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from typing import List

from app import schemas, models, oauth2
from app.database import get_db

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

# --------- Create Post ---------
@router.post("/", response_model=schemas.PostOut)
def create_post(
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    new_post = models.Post(
        title=post.title,
        content=post.content,
        owner_id=current_user.id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# --------- Get All Posts (Owned by current user only) ---------
@router.get("/", response_model=List[schemas.PostOut])
def get_all_posts(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    return db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()


# --------- Get Single Post ---------
@router.get("/{post_id}", response_model=schemas.PostOut)
def get_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(oauth2.get_current_user)
):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to view this post")

    return post


# --------- Update Post ---------
@router.put("/posts/{id}", response_model=schemas.Post)
def update_post(
    id: int,
    updated_post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user),
):
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this post")

    post.title = updated_post.title
    post.content = updated_post.content
    post.published = updated_post.published
    db.commit()
    db.refresh(post)

    return post


# --------- Delete Post ---------
@router.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.UserOut = Depends(oauth2.get_current_user),
):
    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this post")

    db.delete(post)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
