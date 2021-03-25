#!/usr/bin/env python3
import sys
sys.path.append('/home/krylovas/python-project-lvl1/brain_games')
import find_nod

import cli


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Find the greatest common divisor of given numbers')
    find_nod.game()
    print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()
