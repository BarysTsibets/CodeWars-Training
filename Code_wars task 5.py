"""You are going to be given a word. Your job is to return the middle character of the word.
If the word's length is odd, return the middle character.
If the word's length is even, return the middle 2 characters. """


def get_middle(s):
    if len(s) % 2 != 0:
        middle_char = s[len(s) // 2]
        return middle_char
    else:
        ind = len(s) // 2
        middle_char = s[ind-1:ind+1]
        return middle_char


get_middle("middle")
get_middle("testing")
get_middle("A")
get_middle("dD")

