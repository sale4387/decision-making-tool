import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    filename="logger_file.log",
    filemode="a",
    encoding="utf-8"
)

logger = logging.getLogger(__name__)