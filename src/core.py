# import libraries
import logging
import json
from pathlib import Path

# import modules
from .config import config
from .notion.notion_api_client import NotionApiClient

logger = logging.getLogger(__name__)


def execute_test_connection(api_key):
    logger.info(f"Test connection...")
    client = NotionApiClient(api_key)
    notion_info = client.test_connection()
    if notion_info:
        notion_bot = notion_info.get("name")
        logger.info(f"Notion's bot: {notion_bot}")
        logger.info(f"Connection test passed...")
        return True
    else:
        logger.critical(f"Connection test failed...")
        return False

def execute_build_dashboard_layout(api_key, parent_page_id):
    try:
        PORJECT_ROOT = Path(__file__).resolve().parent.parent
        schema_path = PORJECT_ROOT / "schema.json"
        logger.info(schema_path)
        with open(schema_path, "r", encoding="utf-8") as f:
            logger.info(f"File loaded...")
            layout_schema = json.load(f)
        layout_payload = layout_schema.get("layout", [])
        logger.info(f"Layout payload loaded...")
        client = NotionApiClient(api_key)
        response = client.append_block_children(parent_page_id, layout_payload)
        if not response:
            logger.error(f"Build dashboard layout failed...")
    except FileNotFoundError as e:
        logger.error(f"Failed to read schema.json...")