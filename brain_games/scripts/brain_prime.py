#!/usr/bin/env python3
import sys
sys.path.append('/home/krylovas/python-project-lvl1/brain_games')
import is_prime
import cli


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Answer "yes" if the number is prime. Otherwise answer "no".')
    is_prime.game()
    print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()