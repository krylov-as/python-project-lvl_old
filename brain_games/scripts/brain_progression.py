#!/usr/bin/env python3
"""Start game brain-progression."""

import brain_games.arifm as arifm
import brain_games.cli as cli


def main():
    """Ask name user. Start Brain Games - brain-prime."""
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('What number is missing in the progression?')
    check = arifm.game()
    if check:
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))



if __name__ == '__main__':
    main()
