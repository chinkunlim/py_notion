# import libraries
import logging

# import modules
from .logging import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def main():
    logger.info("info")
    logger.debug("debug")
    logger.error("error")
    logger.warning("warning")


if __name__ == "__main__":
    main()