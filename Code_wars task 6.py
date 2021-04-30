"""Move the first letter of each word to the end of it,
then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !"""


def pig_it(text):
    punctuation = "!\" # $%&'()*+, -./:;<=>?@[\]^_`{|}~"
    list_text = text.split()
    # print(list_text)
    new_list = []
    for word in list_text:
        if word not in punctuation:
            first = word[0]
            middle = word[1:]
            result = middle + first + "ay"
            new_list.append(result)
        else:
            new_list.append(word)
    final_phrase = " ".join(new_list)
    return final_phrase




pig_it('Pig, latin is cool !')

# name = "mark"
# first = name[0]
# middle = name[1:]
# result = middle + first + "ay"
# print(result)
