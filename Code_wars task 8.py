"""You are going to be given a word. Your job is to return the middle character of the
word. If the word's length is odd, return the middle character. If the word's length
is even, return the middle 2 characters. """


def get_middle(s):
    if len(s) % 2 == 0:
        print(f'{s} is not odd')

    #logic for 1 character
    elif len(s) == 1:
        print(f'{s} is middle character')

    else:
        print(f'{s} is odd')


get_middle('h')
