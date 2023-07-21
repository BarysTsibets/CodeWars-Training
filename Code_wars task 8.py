"""You are going to be given a word. Your job is to return the middle character of the
word. If the word's length is odd, return the middle character. If the word's length
is even, return the middle 2 characters. """


def get_middle(s):
    if len(s) % 2 == 0:
        first_index = len(s)//2
        second_index = first_index + 1
        print(f'{first_index} first index')
        print(f'{second_index} second index')
        print(s[first_index - 1: first_index + 1])
        return s[first_index - 1: first_index + 1]
        print(f'{s} is not odd')

    #logic for 1 character
    elif len(s) == 1:
        return s
        print(f'{s} is middle character')

    elif len(s)%2 != 0:
        middle_char = len(s)//2
        print(s[middle_char])
        return s[middle_char]
        print(f'{s[middle_char]}')
        print(f'{s} is odd')


get_middle('hel')

# listt = [1,3,7,"this",3,"that", 7]
# # use // Floor Division
# middle = len(listt)//2
# print(middle)
