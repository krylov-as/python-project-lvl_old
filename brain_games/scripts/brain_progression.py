#!/usr/bin/env python3
"""Start game brain-progression."""

import sys
sys.path.append('/home/krylovas/python-project-lvl1/brain_games')
import arifm
import cli


def main():
    """Ask name user. Start Brain Games - brain-prime."""
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('What number is missing in the progression?')
    arifm.game()
    print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()
