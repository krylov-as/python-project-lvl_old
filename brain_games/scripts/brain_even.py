#!/usr/bin/env python3
"""Start game brain-even."""

import brain_games.is_even as is_even
import brain_games.cli as cli


def main():
    """Ask name user. Start Brain Games - brain-prime."""
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    is_even.game()
    print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()
