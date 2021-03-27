#!/usr/bin/env python3
"""Start game brain-prime."""

import brain_games.cli as cli
import brain_games.is_prime as is_prime


def main():
    """Ask name user. Start Brain Games - brain-prime."""
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Answer "yes" if the number is prime. Otherwise answer "no".')
    check = is_prime.game()
    if check:
        print('Congratulations, {}!'.format(name))
    else:
        print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()
