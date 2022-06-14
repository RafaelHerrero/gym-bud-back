from fastapi import APIRouter, Body, Response, status
from lib.core.user_rules import User
from lib.helper.hash_values import HashValues

router = APIRouter()

@router.post("/create", tags=["create user"])
async def create_user(response: Response, payload=Body(...)):
    user = User()
    insert_operation = user.create_user(payload=payload)
    if insert_operation["error"] == "":
        response.status_code = status.HTTP_201_CREATED
    return insert_operation

@router.delete("/delete", tags=["Delete User by ID"])
async def delete_user(payload=Body(...)):
    user = User()
    delete_operation = user.delete_user(user_id=payload["user_id"])
    return delete_operation

@router.get("/all", tags=["get user"])
async def get_all_users():
    user = User()
    get_all = user.get_all_users()
    return get_all

@router.get("/{_id}", tags=["get user by id"])
async def get_user(_id):
    user = User()
    this_user = user.get_user(_id, "user_id")
    return this_user

@router.post("/login", tags=["login user"], status_code=200)
async def login_user(payload=Body(...)):
    user = User()
    user_login = user.get_user(payload["user_login"], "user_login")
    print(user_login)
    if "error" not in user_login.keys():
        return_value = validate_password(user_login, payload["user_password"])
        return return_value
    else:
        return user_login

def validate_password(existing_user: dict, new_pass: str) -> dict:
    new_hash_pass = HashValues().create_hash(new_pass)
    if new_hash_pass == existing_user["user_password"]:
        return_value = {
            "user_id": existing_user["user_id"],
            "user_firstname": existing_user["user_firstname"],
            "error": ""
            }
    else:
        return_value = {"error": "wrong password"}

    return return_value
