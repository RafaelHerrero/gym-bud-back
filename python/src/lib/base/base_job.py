from lib.logger.struct_log import StructLog
from config import Config
from abc import ABC
import argparse
import sys
from lib.helper.hash_values import HashValues
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class BaseJob(ABC):
    def __init__(self) -> None:
        self.config = Config()
        self.hash = HashValues()
        self.logger = StructLog(self.config.LOG_LEVEL, self.config.ENV)
        self.parser = argparse.ArgumentParser(description=self.config.DESCRIPTION)
        self.create_db_session()
        self.logger.info(f"Init {self.config.JOB_NAME} Job")

    # @abstractmethod
    # def execute(self):
    #     pass

    def create_db_session(self):
        self.engine = create_engine(self.config.DB)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
