import logging

DEFAULT_LOG_LEVEL = logging.DEBUG

class BaseLogFormatter(logging.Formatter):

    def __init__(self, fmt: str, datefmt: str) -> None:
        super().__init__(fmt, datefmt)

    def format(self, record: logging.LogRecord) -> str:
        record.shortname = record.name.split('.')[-1]  # type: ignore
        return super().format(record)


def setup_logger(log_level = logging.DEBUG):
    logger = logging.getLogger()
    logger.setLevel(log_level)
    stream_handler = logging.StreamHandler()

    formatter = BaseLogFormatter(
        fmt='%(levelname)8s  %(asctime)s  %(name)20s  %(message)s',
        datefmt='%m-%d %H:%M:%S'
    )

    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)



class BaseLoggingService():
    _logger = None

    @property
    def logger(self):
        if self._logger is None:
            self._logger = logging.getLogger(self.__module__ + '.' + self.__class__.__name__)
        return self._logger