import logging
import os

def get_logger():
    logger = logging.getLogger("automation")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    os.makedirs("logs", exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler = logging.FileHandler("logs/automation.log", mode="a")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
