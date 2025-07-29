"""Entry point for running the agent application from the command line."""

from argparse import ArgumentParser
from typing import List, Optional

from .agent import Agent


def main(argv: Optional[List[str]] = None) -> None:
    """Run the agent application as a script.

    Parameters
    ----------
    argv:
        Optional list of command line arguments. If ``None`` (the default),
        ``sys.argv`` is used implicitly by ``ArgumentParser``.
    """

    parser = ArgumentParser(description="Run the agent application")
    parser.add_argument(
        "--name",
        default="Demo",
        help="Name of the agent",
    )
    args = parser.parse_args(argv)

    agent = Agent(name=args.name)
    print(agent.run())


if __name__ == "__main__":
    main()
