"""QA entry point â€” main application module."""
import sys
from src.utils.helpers import greet
from src.utils.constants import APP_NAME, VERSION


def main():
    print(f"{APP_NAME} v{VERSION}")
    greet("world")
    return 0


if __name__ == "__main__":
    sys.exit(main())
