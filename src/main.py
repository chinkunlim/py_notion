# import libraries
import logging

# import modules
from .logging import setup_logging
from .config import config
from .core import *

setup_logging()
logger = logging.getLogger(__name__)


config.load_env()
env = config.get_env()
api_key = env.get("NOTION_API_KEY")
parent_page_id = env.get("PARENT_PAGE_ID")

def main():
    # logger.info("info")
    # logger.debug("debug")
    # logger.error("error")
    # logger.warning("warning")
    # config.set_env("abc","456")

    execute_test_connection(api_key)
    execute_delete_blocks(api_key, parent_page_id)
    execute_build_dashboard_layout(api_key, parent_page_id)
    execute_create_database(api_key, parent_page_id)

if __name__ == "__main__":
    main()