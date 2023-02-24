from fastapi import APIRouter, status, Response
from config.db import conn
from models.user import users 
from schemas.user import User
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import text

user = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)

@user.get("/users", response_model=list[User], description="Get a list of all users", tags=["users"])
def get_users():
    return conn.execute(users.select()).mappings().all()

@user.get("/users/count",response_model=int ,description="Get the number of users", tags=["users"])
def count_users():
    return conn.execute(text("SELECT count(*) from users")).scalar()

@user.post("/users",  response_model=User,
    description="Create a new ser", tags=["users"])
def create_user(user:User):
    new_user = {"name":user.name, "email":user.email}
    new_user['password'] = f.encrypt(user.password.encode('utf-8'))
    result = conn.execute(users.insert().values(new_user))
    conn.commit()
    l_conn = conn.execute(users.select().where(users.c.id == result.lastrowid)).mappings().first()
    return l_conn

@user.get("/users/{id}", response_model=User, description="Get a user by id", tags=["users"])
def get_user(id:str):
    return conn.execute(users.select().where(users.c.id == id)).mappings().first()

@user.delete("/users/{id}", status_code=HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(id:str):
    conn.execute(users.delete().where(users.c.id == id))
    conn.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    
@user.put("/users/{id}", response_model=User, description="Update a user by id", tags=["users"])
def update_user(id:str, user:User):
    conn.execute(users.update().where(users.c.id == id).values(name=user.name, email=user.email, 
    password=f.encrypt(user.password.encode('utf-8'))))
    conn.commit()
    return conn.execute(users.select().where(users.c.id == id)).mappings().first()
   
