#!/usr/bin/env python3
"""Start brain-games."""

import brain_games.cli as cli


def welcome():
    """Print welcome text."""
    print('Welcome to the Brain Games!')


def main():
    """Print welcome text and name user."""
    welcome()
    cli.welcome_user()


if __name__ == '__main__':
    main()
