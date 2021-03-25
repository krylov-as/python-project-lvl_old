#!/usr/bin/env python3
"""Start game brain-even."""

import sys

sys.path.append('/home/krylovas/python-project-lvl1/brain_games')
import is_even
import cli


def main():
    """Ask name user. Start Brain Games - brain-prime."""
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    is_even.game()
    print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()
