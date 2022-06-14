from sqlalchemy import Table, insert


class DbServices:
    def __init__(self, engine) -> None:
        self.engine = engine

    def insert_values(self, table: Table, value: dict, return_value: str) -> list:
        return_obj = getattr(table, return_value)
        sql = insert(table).values(**value).returning(return_obj)
        result = self.engine.execute(sql)
        response = [dict(row) for row in result]

        return response
