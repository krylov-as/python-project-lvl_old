#!/usr/bin/env python3
import sys
sys.path.append('/home/krylovas/python-project-lvl1/brain_games')
import find_nod
import cli


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    find_nod.game()
    print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()