"""You are going to be given a word. Your job is to return the middle character of the
word. If the word's length is odd, return the middle character. If the word's length
is even, return the middle 2 characters. """


def get_middle(s):
    # logic for Not Odd length
    if len(s) % 2 == 0:
        first_index = len(s) // 2
        second_index = first_index + 1
        return s[first_index - 1: second_index]

    # logic for Odd length
    elif len(s) % 2 != 0:
        middle_char = len(s) // 2
        return s[middle_char]

    # logic for 1 character
    elif len(s) == 1:
        return s
        # print(f'{s} is middle character')

    else:
        print('hello world')


get_middle('hello')