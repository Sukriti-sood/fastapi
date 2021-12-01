from sqlalchemy.sql.functions import func
from .. import models,schema, oauth2
from typing import List, Optional
from fastapi import  Response, status, HTTPException, Depends,APIRouter
from sqlalchemy.orm import Session
from ..database import get_db


router= APIRouter(
    prefix="/posts",
    tags=['Posts']
)



# response_model=List[schema.Post]
@router.get("/",response_model=List[schema.PostOut])
def get_posts(db: Session = Depends(get_db), limit :int = 10, skip: int = 0, search: Optional[str] = ""):
    # cursor.execute("""SELECT * FROM posts;""")
    # posts = cursor.fetchall()
    # print(search)
    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit=limit).offset(skip).all()
    
    result= db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(
            models.Post.id
        ).filter(models.Post.title.contains(search)).limit(limit=limit).offset(skip).all()

    return result


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.Post)
def create_posts(post: schema.PostCreate, db: Session = Depends(get_db),current_user:schema.UserOut= Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *;""",(post.title,
    # post.content, post.published))
    # new_post=cursor.fetchone()
    # conn.commit()

    # instead of writing all field and values we can use:-
    # **post.dict()
    #new_post= models.Post(title=post.title, content= post.content, published= post.published)
    new_post = models.Post(**post.dict(), owner_id = current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# order matters
# @router.get("/posts/latest")
# def get_latest_post():
#     return {"post":my_posts[len(my_posts)-1]}


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schema.PostOut)
# or (str(id)) here
def get_post(id: int, response: Response, db: Session = Depends(get_db), current_user:schema.UserOut= Depends(oauth2.get_current_user)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s;""",[id])
    # post=cursor.fetchone()
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(
            models.Post.id
        ).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} not found")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {"message":f"post with id: {id} not found"}
    return post


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user:int= Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *;""",[id])
    # deleted_post=cursor.fetchone()
    # conn.commit()
    post = db.query(models.Post).filter(models.Post.id == id)

    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No such Post available")

    if post.first().owner_id!= current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform this action")

    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schema.Post)
def update_post(id: int, updated_post: schema.PostCreate, db: Session = Depends(get_db), current_user:schema.UserOut= Depends(oauth2.get_current_user)):
    # cursor.execute("""UPDATE posts SET title= %s, content= %s,published= %s
    # WHERE id=%s RETURNING *""",(post.title,post.content,post.published,str(id)))
    # updated_post=cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="No such Post available")

    if post.owner_id!= current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform this action")

    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()