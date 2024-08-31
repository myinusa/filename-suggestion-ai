import argparse
import sys


def get_parsed_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        # description=DESC,  # Program description
        # formatter_class=RichHelpFormatterPlus,  # Disable line wrapping
        allow_abbrev=False,  # Disable abbreviations
        add_help=False,  # Disable default help
    )

    # parser.add_argument("--playlist", action="store_true", help="playlist process.")
    # parser.add_argument("--video_items", action="store_true", help="List of video items to process.")

    g_misc = parser.add_argument_group("Miscellaneous Options")
    # Help
    g_misc.add_argument("-h", "--help", action="help", help="Show this help message and exit.")
    # Verbose
    g_misc.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        action="store_true",
        default=False,
        help="Show log messages on screen. Default is False.",
    )
    # Debug
    g_misc.add_argument(
        "-d",
        "--debug",
        dest="debug",
        action="store_true",
        default=False,
        help="Activate debug logs. Default is False.",
    )

    args = parser.parse_args()

    # Conditional check to ensure at least one argument is provided
    # if not args.playlist and not args.video_items:
    #     print("Error: At least one of --playlist or --video_items must be provided.")
    #     parser.print_help()
    #     sys.exit(1)

    return args
