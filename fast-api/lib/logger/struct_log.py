import structlog
import logging


class StructLog:
    def __init__(self, log_level=logging.INFO, env="production"):
        structlog.configure(
            cache_logger_on_first_use=True,
            wrapper_class=structlog.make_filtering_bound_logger(min_level=log_level),
            processors=self.__get_processor_by_env(env),
        )
        self.logger = structlog.get_logger()

        global logger
        logger = self.logger

    def __get_processor_by_env(self, env="production"):
        list_processors = [
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso", utc=True),
        ]
        if env == "dev" or env == "development":
            list_processors.append(structlog.processors.StackInfoRenderer())
            list_processors.append(structlog.dev.ConsoleRenderer())
        else:
            list_processors.append(structlog.processors.JSONRenderer())
        return list_processors

    def info(self, msg, obj=None):
        self.logger.info(msg, obj=obj)

    def error(self, msg, obj=None):
        self.logger.error(msg, obj=obj)

    def debug(self, msg, obj=None):
        self.logger.debug(msg, obj=obj)

    def warning(self, msg, obj=None):
        self.logger.warning(msg, obj=obj)

    def exception(self, exception):
        self.logger.exception(exception)
        raise Exception
