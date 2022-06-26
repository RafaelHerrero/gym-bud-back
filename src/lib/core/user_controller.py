from fastapi import Response, status
from lib.models.models import UserTable, CreateUser
from lib.base.base_job import BaseJob
from lib.errors.errors import UserNotFoundError, PasswordNotFoundError
from lib.helper.hash_values import HashValues


class UserController(BaseJob):
    def __init__(self) -> None:
        super().__init__()
        self.table = UserTable

    def create_user(self, payload: CreateUser):
        new_user = self.table()
        new_user.user_id = self.hash.create_uuid()  # type: ignore
        new_user.user_firstname = payload.user_firstname  # type: ignore
        new_user.user_lastname = payload.user_lastname  # type: ignore
        new_user.user_login = payload.user_login  # type: ignore
        new_user.user_password = self.hash.create_hash(payload.user_password)  # type: ignore
        with self.session_factory() as session:
            entity: UserTable = session.query(self.table).filter(
                self.table.user_login == payload.user_login).first()
            if not entity:
                session.add(new_user)
                session.commit()
                session.refresh(new_user)
                return new_user
            else:
                return Response(status_code=status.HTTP_409_CONFLICT)

    def delete_user(self, user_id: str):
        with self.session_factory() as session:
            entity: UserTable = session.query(self.table).filter(
                self.table.user_id == user_id).first()
            if not entity:
                raise UserNotFoundError(user_id)
            session.delete(entity)
            session.commit()

    def get_user(self, value: str, column: str) -> dict:
        attrs = getattr(self.table, column)
        with self.session_factory() as session:
            entity: UserTable = session.query(self.table).filter(
                attrs == value).first()
            if not entity:
                raise UserNotFoundError(value)

            return entity

    def get_all_users(self) -> list:
        with self.session_factory() as session:
            return session.query(self.table).all()

    def login_user(self, payload):
        existing_user = self.get_user(payload.user_login, "user_login")
        hash_pw = HashValues().create_hash(payload.user_password)
        if hash_pw == existing_user.user_password:  # type: ignore
            return existing_user
        else:
            raise PasswordNotFoundError(payload.user_login)

