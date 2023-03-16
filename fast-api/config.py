import os
import logging


class Config:
    JOB_NAME = "Gym Bud Back"
    DESCRIPTION = "Gym Bud Backend"
    ENV = os.getenv("ENV", "dev")
    LOG_LEVEL = os.getenv("LOGLEVEL", logging.INFO)
    DEBUG = os.getenv("DEBUG", False)
    DB = os.getenv("DB", "postgresql://postgres:postgres@127.0.0.1:5432/main")
