from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/") ## ----> Decorator that turns this into an actual path operation. ".get" is the menthod and "/" is the path or url
async def root():
    return {"message":"Hello"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your post"}


@app.post("/createpost")
#def create_post(payload: dict = Body(...)):    # extracting data 
def create_post(new_post: Post):
    #print(payload)
    print(new_post.title)
    print(new_post.published)
    print(new_post.dict())
    #return {"new_post":f"title {payload['title']} content: f{payload['content']}"}
    return {"data": new_post}
    #return {"data": "new_post"}
# title -> str, content -> str