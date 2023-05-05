#!/usr/bin/env python3
"""
Author : echeadle <echeadle@localhost>
Date   : 2023-05-01
Purpose: File Tracker
"""

import argparse
import os
import shlex

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='File Tracking Application',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')
    return parser.parse_args()
    


def is_file_or_dir(path):
    if os.path.isfile(path):
        print(path, "is a file")
    elif os.path.isdir(path):
        print(path, "is a directory")
    else:
        print(path, "is not a file or directory")

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg = args.positional
    is_file_or_dir(pos_arg)

#    print(f'positional = "{shlex.quote(pos_arg)}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()

