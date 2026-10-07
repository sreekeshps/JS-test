"""Integration test: end-to-end agent flow with mocked LLM."""
import sys
from types import ModuleType
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from langchain_core.messages import AIMessage

# ---------------------------------------------------------------------------
# Stub out modules that are unavailable in the test environment
# ---------------------------------------------------------------------------

# sap_cloud_sdk.agent_memory.factory is not present in the test SDK version;
# create a minimal stub so agent.py can be imported.
_factory_stub = ModuleType("sap_cloud_sdk.agent_memory.factory")
_checkpoint_stub = ModuleType("sap_cloud_sdk.agent_memory.factory.langgraph_checkpoint")
_checkpoint_stub.create_checkpointer = MagicMock(return_value=None)
sys.modules.setdefault("sap_cloud_sdk.agent_memory.factory", _factory_stub)
sys.modules.setdefault(
    "sap_cloud_sdk.agent_memory.factory.langgraph_checkpoint", _checkpoint_stub
)




@pytest.mark.asyncio
async def test_agent_invoke_hello_world():
    """Test that the agent processes a test task and returns a completed response."""
    from agent import SampleAgent

    mock_result = {
        "messages": [
            AIMessage(
                content='{"status": "passed", "task": "hello-world", "result": "Hello, World! Test executed successfully."}'
            )
        ]
    }

    agent = SampleAgent()

    with patch.object(
        agent, "_invoke_with_fallback", new_callable=AsyncMock, return_value=mock_result
    ):
        response = await agent.invoke("Run the hello world test", context_id="test-ctx-1")

    assert response.status == "completed"
    assert response.message is not None
    assert len(response.message) > 0


@pytest.mark.asyncio
async def test_agent_stream_yields_completed():
    """Test that stream() yields a completed chunk."""
    from agent import SampleAgent

    mock_result = {
        "messages": [AIMessage(content="Hello, World! Test executed successfully.")]
    }

    agent = SampleAgent()

    with patch.object(
        agent, "_invoke_with_fallback", new_callable=AsyncMock, return_value=mock_result
    ):
        chunks = []
        async for chunk in agent.stream(
            "Run the hello world test", context_id="test-ctx-2"
        ):
            chunks.append(chunk)

    assert len(chunks) >= 2
    final = chunks[-1]
    assert final["is_task_complete"] is True
    assert "Hello, World!" in final["content"]


@pytest.mark.asyncio
async def test_agent_invoke_error_handling():
    """Test that agent handles errors gracefully."""
    from agent import SampleAgent

    agent = SampleAgent()

    with patch.object(
        agent,
        "_invoke_with_fallback",
        new_callable=AsyncMock,
        side_effect=RuntimeError("LLM unavailable"),
    ):
        response = await agent.invoke("Run a test", context_id="test-ctx-3")

    # On exception, stream() yields is_task_complete=True with an error message
    # (graceful degradation), so invoke() maps this to "completed"
    assert response.status in ("error", "completed")
    assert "error" in response.message.lower()
