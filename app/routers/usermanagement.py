from datetime import datetime
from xmlrpc.client import DateTime

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.deps.dependencies import get_token_header

router = APIRouter(
    prefix="/usermanagement",
    tags=["usermanagement"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}, 401: {"description":"X-Token header invalid"}},
)

fake_users_db = {"admin":"administrative users", "testuser":"test user"}

class CreateUserRequest(BaseModel):
    username: str
    description: str
    created_by: str

class CreateUserResponse(BaseModel):
    username: str
    description: str
    created_by: str
    created: datetime

@router.get("/users", tags=["usermanagement"])
async def read_users():
    return [{"username": "admin", "description":fake_users_db.get("admin")}, {"username": "testuser", "description":fake_users_db.get("testuser")}]

@router.get("/users/{username}", tags=["usermanagement"])
async def read_user(username: str):
    return {"username": username, "description":fake_users_db.get(username)}

@router.post("/users", tags=["usermanagement"])
async def create_user(user:CreateUserRequest) -> CreateUserResponse:
    print("here is the username: "+user.username)
    print("here is the description: "+user.description)
    print("here is the creator: "+user.created_by)
    return CreateUserResponse(username=user.username,description=user.description,created_by=user.created_by,created=datetime.now())