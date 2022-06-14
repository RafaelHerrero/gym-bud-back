from lib.logger.struct_log import StructLog
import os
import logging

if not "logger" in globals():
    global logger
    logger = StructLog(os.getenv("LOGLEVEL", logging.INFO), os.getenv("ENV", "prod"))
