import argparse
import sys


def get_parsed_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        allow_abbrev=False,
        add_help=False,
    )

    g_misc = parser.add_argument_group("Miscellaneous Options")
    g_misc.add_argument("-h", "--help", action="help", help="Show this help message and exit.")
    g_misc.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        default=False,
        help="Show log messages on screen. Default is False.",
    )
    g_misc.add_argument(
        "-d",
        "--debug",
        dest="debug",
        action="store_true",
        default=False,
        help="Activate debug logs. Default is False.",
    )
    # New argument for file input
    g_misc.add_argument(
        "-f",
        "--file",
        dest="file",
        required=True,
        help="Path to the file whose content will be sent as user content in the payload.",
    )

    args = parser.parse_args()

    return args