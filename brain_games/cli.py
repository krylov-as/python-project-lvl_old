"""Ask user name"""
import prompt


def welcome_user():
    """Ask user name"""
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name
