"""Unit tests for the run_hello_world_test tool."""
import pytest
from tools import run_hello_world_test


def test_run_hello_world_test_returns_passed_status():
    result = run_hello_world_test.invoke({"task": "my-test"})
    assert result["status"] == "passed"


def test_run_hello_world_test_echoes_task():
    result = run_hello_world_test.invoke({"task": "smoke-test"})
    assert result["task"] == "smoke-test"


def test_run_hello_world_test_contains_greeting():
    result = run_hello_world_test.invoke({"task": "hello"})
    assert "Hello, World!" in result["result"]


def test_run_hello_world_test_success_message():
    result = run_hello_world_test.invoke({"task": "e2e"})
    assert "successfully" in result["result"]


def test_run_hello_world_test_result_keys():
    result = run_hello_world_test.invoke({"task": "full-check"})
    assert set(result.keys()) == {"status", "task", "result"}
