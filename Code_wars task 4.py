"""Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic
characters and numeric digits that occur more than once in the input string.
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice"""


def duplicate_count(random_text):
    random_text = random_text.lower()
    duplicates = []
    for char in random_text:
        if random_text.count(char) > 1:
            if char not in duplicates:
                duplicates.append(char)

    # print(len(duplicates))
    return len(duplicates)


duplicate_count("abcde")
duplicate_count("Indivisibilities")
duplicate_count("aabb1cde122")


