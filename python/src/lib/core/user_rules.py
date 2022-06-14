from sqlalchemy import insert, select
from lib.models.user_model import UserTable
from lib.logger.struct_log import logger
from lib.base.base_job import BaseJob


class User(BaseJob):
    def __init__(self) -> None:
        super().__init__()
        self.table = UserTable

    def create_user(self, payload: dict) -> dict:
        new_user = {}
        new_user["user_id"] = self.hash.create_uuid()
        new_user["user_firstname"] = payload['user_firstname']
        new_user["user_lastname"] = payload['user_lastname']
        new_user["user_login"] = payload['user_login']
        new_user["user_password"] = self.hash.create_hash(payload["user_password"])
        sql = insert(self.table).values(**new_user)
        try:
            self.engine.execute(sql)
            return_value = {
                "user_id": new_user["user_id"],
                "user_firstname": new_user["user_firstname"],
                "error": ""
                }

        except Exception as e:
            logger.error(f"Failed to Insert: {e}")
            return_value = {"error": "Failed to insert User, already exists"}

        return return_value

    def delete_user(self, user_id: str) -> dict:
        effected_rows = self.session.query(self.table) \
                .filter(self.table.user_id==user_id).delete()
        if effected_rows == 0:
            logger.error("Failed to delete user")
            return_value = {"error": "Failed to Delete User"}
        else:
            return_value = {"error": ""}

        return return_value

    def get_user(self, user_id: str, column: str) -> dict:
        attrs = getattr(self.table, column)
        sql = select(self.table).where(attrs == user_id)
        try:
            this_user = self.engine.execute(sql).one()
        except Exception as e:
            logger.error(e)
            this_user = {"error": "No User with id"}

        return this_user  # type: ignore

    def get_all_users(self) -> list:
        sql = select(self.table)
        all_users = self.engine.execute(sql).fetchall()
        return all_users
