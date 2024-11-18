from fastapi import FastAPI

app = FastAPI()

from enum import Enum

@app.get("/")
async def root():
    return {"message":"hello world"}

@app.post("/")
async def post():
    return {"message":"this is a post request"}

@app.put("/", description="this is a put endpoint")
async def put():
    return {"message":"this is a put request"}

@app.get("/users")
async def list_users():
    return {"message":"this is users list"}

@app.get("/users/1" , include_in_schema=False)
async def admin_user():
    return {"message ":"this is the admin portal"}

@app.get("/users/{user_id}")
async def get_user(user_id : int ):
    return {"user id":user_id}

class UsersList(str ,Enum):
    admin = 1
    manger = 2
    user = 3

@app.get("/{user_type}/{user_id}")
async def get_user_type(user_type : UsersList , user_id):
    return {"user ": {user_type , user_id}}
