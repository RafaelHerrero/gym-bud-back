from fastapi import APIRouter, Body, status, Response
from lib.core.user_rules import UserService
from lib.models.user_model import CreateUser, UserId, LoginUser

router = APIRouter()

@router.post("/create", tags=["Users Routes"], status_code=status.HTTP_201_CREATED)
async def create_user(payload: CreateUser = Body(...)):
    user = UserService()
    return user.create_user(payload=payload)

@router.delete("/delete", tags=["Users Routes"])
async def delete_user(payload: UserId = Body(...)):
    user = UserService()
    try:
        user.delete_user(payload.user_id)
    except:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get("/all", tags=["Users Routes"])
async def get_all_users():
    user = UserService()
    return user.get_all_users()

@router.get("/{_id}", tags=["Users Routes"])
async def get_user(_id):
    user = UserService()
    return user.get_user(_id, "user_id")

@router.post("/login", tags=["Users Routes"], status_code=200)
async def login_user(payload: LoginUser = Body(...)):
    user = UserService()
    try:
        existing_user = user.login_user(payload)
    except:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return existing_user

