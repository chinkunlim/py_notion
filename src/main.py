# import libraries
import logging

# import modules
from .logging import setup_logging
from .config import config

setup_logging()
logger = logging.getLogger(__name__)

def main():
    logger.info("info")
    logger.debug("debug")
    logger.error("error")
    logger.warning("warning")

    config.load_env()
    env = config.get_env()
    api_key = env.get("NOTION_API_KEY")
    print(api_key)
    config.set_env("abc","456")

if __name__ == "__main__":
    main()