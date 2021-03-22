#!/usr/bin/env python3
import sys
sys.path.append('/home/krylovas/python-project-lvl1/brain_games')
import cli
import calc



def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    print('What is the result of the expression?')
    calc.game()
    print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()