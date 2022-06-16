from lib.logger.struct_log import StructLog
from config import Config
from abc import ABC
import argparse
import sys
from lib.helper.hash_values import HashValues
from sqlalchemy import create_engine, orm
from sqlalchemy.orm import sessionmaker


class BaseJob(ABC):
    def __init__(self) -> None:
        self.config = Config()
        self.hash = HashValues()
        self.logger = StructLog(self.config.LOG_LEVEL, self.config.ENV)
        self.parser = argparse.ArgumentParser(description=self.config.DESCRIPTION)
        self.create_db_session()

    # @abstractmethod
    # def execute(self):
    #     pass

    def create_db_session(self):
        self.engine = create_engine(self.config.DB)
        self.session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.engine,
            ),
        )
