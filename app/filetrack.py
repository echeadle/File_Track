#!/usr/bin/env python3
"""
Author : echeadle <echeadle@localhost>
Date   : 2023-05-01
Purpose: File Tracker
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='File Tracker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('-d',
                        '--dir',
                        help='Directory/folder to scan',
                        metavar='str',
                        type=str,
                        default='/home/echeadle/Ansible')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """File Track manin function"""

    args = get_args()
    str_arg = args.dir

    print(f'str_arg = "{str_arg}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
