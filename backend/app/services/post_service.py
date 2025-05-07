from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate

def get_all_posts(db: Session):
    return db.query(Post).all()

def create_post(db: Session, post_data: PostCreate):
    post = Post(**post_data.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
