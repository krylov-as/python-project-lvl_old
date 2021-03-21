#!/usr/bin/env python
import sys
sys.path.append('/home/krylovas/python-project-lvl1/brain_games')

import cli

def welcome():
    print('Welcome to the Brain Games!')
    

def main():
    welcome()
    cli.welcome_user()


if __name__ == '__main__':
    main()
