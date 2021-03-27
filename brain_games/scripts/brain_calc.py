#!/usr/bin/env python3
"""Start game brain-calc."""

import brain_games.cli as cli
import brain_games.calc as calc


def main():
    """Ask name user. Start Brain Games - brain-calc."""
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('What is the result of the expression?')
    check = calc.game()
    if check:
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()
