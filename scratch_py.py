with open("asdf\\book1.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(text.count("the"))
print(text.count("the "))
print(text.count(" the"))
print(text.count(" the "))
# print("!")
# print("!")
# print("!")
# print("!")
# print("!")