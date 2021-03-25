#!/usr/bin/env python3
"""Start brain-games."""


import sys

sys.path.append('/home/krylovas/python-project-lvl1/brain_games')

import cli


def welcome():
    """Print welcome text."""
    print('Welcome to the Brain Games!')


def main():
    """Print welcome text and name user."""
    welcome()
    cli.welcome_user()


if __name__ == '__main__':
    main()
