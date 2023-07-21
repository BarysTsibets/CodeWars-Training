"""Your job is to write a function which increments a string, to create a new string.
If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.

Examples:
foo -> foo1
foobar23 -> foobar24
foo0042 -> foo0043
foo9 -> foo10
foo099 -> foo100
Attention: If the number has leading zeros the amount of digits should be considered."""


def increment_string(strng):
    if strng[-1:].isdigit():
        last_digits_int = ""
        for i in reversed(strng):
            if i.isdigit():
                last_digits_int = last_digits_int + str(i)
            else:
                break
        dig_str = last_digits_int[::-1]
        last_digits_int = int(last_digits_int[::-1])
        new_digit = last_digits_int + 1
        #     for case : foobar325  and foobar099
        if len(str(dig_str)) == len(str(new_digit)):
            strng = strng[:-len(str(new_digit))] + str(new_digit)
        # for case : foobar99
        elif len(str(new_digit)) > len(str(last_digits_int)) and len(str(dig_str)) < len(str(new_digit)):
            strng = strng[:-len(str(last_digits_int))] + str(new_digit)
            # for  Case foobar3
        elif len(str(last_digits_int)) == len(str(new_digit)):
            strng = strng[:-len(str(new_digit))] + str(new_digit)
            # for  Case foobar009
        elif len(str(dig_str)) > len(str(new_digit)):
            strng = strng[:-len(str(new_digit))] + str(new_digit)
        else:
            strng = strng[:-len(str(new_digit)) + 1] + str(new_digit)
            # case foo
    else:
        strng = strng + "1"
    return strng


# strng = "foo"
# strng = "foobar3"
# strng = "foobar000"
strng = "foobar99"
print(increment_string(strng))


# Notes added