#!/usr/bin/env python3
"""Start game brain-gcd."""

import brain_games.cli as cli
import brain_games.find_nod as find_nod


def main():
    """Ask name user. Start Brain Games - brain-prime."""
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Find the greatest common divisor of given numbers')
    find_nod.game()
    print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()
