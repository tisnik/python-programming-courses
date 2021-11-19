#!/usr/bin/env python3

from argparse import ArgumentParser

def cli_arguments():
    """Retrieve all CLI arguments provided by user."""
    # First of all, we need to specify all command line flags that are
    # recognized by this tool.
    parser = ArgumentParser()

    # All supported command line arguments and flags
    parser.add_argument("-a", "--address", dest="address", required=False,
                        help="Address of REST API for external data pipeline")

    parser.add_argument("-u", "--user", dest="user", required=False,
                        help="User name for basic authentication")

    parser.add_argument("-p", "--password", dest="password", required=False,
                        help="Password for basic authentication")

    parser.add_argument("-i", "--input", dest="input", default=None, required=False,
                        help="Specification of input file (with list of clusters, for example)")

    parser.add_argument("-c", "--compare-results", dest="compare_results", action="store_true",
                        default=None, required=False,
                        help="Compare two sets of results, each set stored in its own directory")

    parser.add_argument("-e", "--export", dest="export_file_name", required=False,
                        default="report.csv",
                        help="Name of CSV file with exported comparison results")

    parser.add_argument("-v", "--verbose", dest="verbose", action="store_true", default=None,
                        help="Make messages verbose", required=False)

    # Now it is time to parse flags, check the actual content of command line
    # and fill-in the object named `args`.
    return parser.parse_args()


def main():
    """Entry point to this script."""
    # Parse and process and command line arguments.
    args = cli_arguments()

    # Verbosity flag
    verbose = args.verbose


# If this script is started from command line, run the `main` function which is
# entry point to the processing.
if __name__ == "__main__":
    main()
