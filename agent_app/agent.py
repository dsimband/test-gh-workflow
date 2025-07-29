"""Core agent implementation."""


class Agent:
    """Simple agent skeleton."""

    def __init__(self, name: str):
        self.name = name

    def run(self) -> str:
        """Perform agent's main action."""
        return f"Agent {self.name} is running"
