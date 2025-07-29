"""Tests for the Agent class."""

from agent_app.agent import Agent


def test_run_returns_expected_message():
    agent = Agent("Test")
    assert agent.run() == "Agent Test is running"


def test_cli_runs(tmp_path, capsys):
    """Verify the command line interface outputs the expected text."""

    from agent_app.main import main

    main(["--name", "CLI"])

    captured = capsys.readouterr()
    assert captured.out.strip() == "Agent CLI is running"
