"""The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!
Here's the deal:
It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false."""


def generate_hashtag(s):
    if s:
        if len(s) <= 140:
            n_list = s.split()
            tag = "#"
            for word in n_list:
                tag = tag + word.capitalize()
        else:
            return False
        return tag
    else:
        return False


s = "Hello there thanks for trying my Kata"
# s = ""
print(generate_hashtag(s))

