from calendar import EPOCH
import logging
from fastapi import APIRouter, Body, HTTPException
from models.user_model import UserTable
import os
from sqlalchemy import create_engine, select, insert, delete
from datetime import datetime
import json 

router = APIRouter()

@router.post("/create_user", tags=["create user"])
async def get_create_user(payload= Body(...)):
    
    new_user = payload[0]
    
    user_id = f'{new_user["user_login"]}'

    user_firstname = new_user['user_firstname']
    user_lastname = new_user['user_lastname']
    user_login = new_user['user_login']
    user_password = new_user['user_password']
    # updated_at = new_user['updated_at']
    # created_at = new_user['created_at']
    engine = create_engine('postgresql://postgres:postgres@127.0.0.1:5432/postgres')
    result = check_data(user_login, engine)
    
    if not result:

    
        
        sql = insert(UserTable).values(
                user_id=user_id, 
                user_firstname=user_firstname, 
                user_lastname=user_lastname, 
                user_login=user_login, 
                user_password=user_password 
                # updated_at=updated_at, 
                # created_at=created_at
            )
        
        engine.execute(sql)
        sql = select(UserTable).where(UserTable.user_login == user_login)
        result = engine.execute(sql)
        result_dict = [dict(t) for t in result]
        print(f'Usuário {result_dict[0]["user_firstname"]} inserido com sucesso')
        return result_dict[0]['user_id']

    else:
        return {'error': f'login {user_login} Já cadastrado'} 

def check_data(login, engine):
    
    sql = select(UserTable).where(UserTable.user_login == f'{login}')
    result = engine.execute(sql)
    result_list = [list(t) for t in result]
    print(f'result : {result_list}')
    bool_result = bool(result_list)
    return bool_result

@router.delete("/delete_user/{login}", tags=["delete user by login"])
async def delete_user(login):
    
    # if check_data(login):
    engine = create_engine('postgresql://postgres:postgres@127.0.0.1:5432/postgres')
    sql = delete(UserTable).where(UserTable.user_login == login).returning(UserTable.user_login)
    result = engine.execute(sql)
    result_list = [t for t in result]
    print(result_list)
    if len(result_list) != 0:
        return 200
    else:
        return f'failed to delete {login}'


@router.get("/all", tags=["get user"])
async def get_user():
    engine = create_engine('postgresql://postgres:postgres@127.0.0.1:5432/postgres')
    sql = select(UserTable)
    
    result =  engine.execute(sql)
    result_dict = [dict(t) for t in result]

    return result_dict 

@router.get("/{id}", tags=["get user by id"])
async def get_user(id):
    engine = create_engine('postgresql://postgres:postgres@127.0.0.1:5432/postgres')
    sql = select(UserTable).where(UserTable.user_id == id)
    result =  engine.execute(sql)
    result_dict = [dict(t) for t in result]

    return result_dict 

# @router.get("/all", tags=["get all"] , )
# async def get_all_users():
#     engine = create_engine('postgresql://postgres:postgres@127.0.0.1:5432/postgres')
#     sql = select(UserTable)
#     result =  engine.execute(sql)
#     result_dict = [dict(t) for t in result]

#     return result_dict 

# @router.get("/{id}", tags=["get id"])
# async def get_users_by_id(id):
#     engine = create_engine('postgresql://postgres:postgres@127.0.0.1:5432/postgres')
    
#     sql = select(UserTable).where(UserTable.user_id == id)
#     result =  engine.execute(sql)
#     result_dict = [dict(t) for t in result]

#     return result_dict
