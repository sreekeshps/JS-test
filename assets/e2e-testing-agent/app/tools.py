import logging
from langchain_core.tools import tool

logger = logging.getLogger(__name__)


@tool
def run_hello_world_test(task: str) -> dict:
    """Run a hello world end-to-end test scenario.

    Args:
        task: The name of the test task to execute.

    Returns:
        A structured result dict with status, task, and result fields.
    """
    logger.info("Running hello world test for task: %s", task)
    return {
        "status": "passed",
        "task": task,
        "result": "Hello, World! Test executed successfully.",
    }
