import logging
from config import LOG_LEVEL

level= getattr(logging, LOG_LEVEL)
logging.getLogger("httpx").setLevel(logging.WARNING) #removes noise in log file from errors from outside
logging.getLogger("httpcore").setLevel(logging.WARNING)

logging.basicConfig(
    level=level,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    filename="logger_file.log",
    filemode="a",
    encoding="utf-8"
)

