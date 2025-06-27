# import libraries
import logging

# import modules
from .config import config
from .notion.notion_api_client import NotionApiClient

logger = logging.getLogger(__name__)

def execute_test_connection(api_key):
    logger.info(f"Test connection...")
    client = NotionApiClient(api_key)
    notion_info = client.test_connection()
    if notion_info:
        logger.info(f"Connection test passed...")
        return True
    else:
        logger.critical(f"Connection test failed...")
        return False