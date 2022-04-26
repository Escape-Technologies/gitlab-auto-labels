"""Lib entrypoint."""
import sys
import argparse

from auto_labels import main


def main_wrapper() -> int:
    """Wrapper for main."""

    parser = argparse.ArgumentParser(prog="auto_labels", description=main.__doc__)
    parser.add_argument("ref1", type=str, help="The source ref you want to compare", default="origin/HEAD")
    parser.add_argument("ref2", type=str, help="The target ref you want to compare", default="HEAD")

    args = parser.parse_args()
    return main.main(args.ref1, args.ref2)


if __name__ == "__main__":
    sys.exit(main_wrapper())
