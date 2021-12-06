"""
"he-llo-wor-ld-sal-am-b-ye-he-llo"
"hello-world-salam-bye-hello"
vorodi = input()
words = vorodi.split("-")
----------------------------------------
hello*world*salam*bye-hello
words = input().split()
['hello', 'world', 'salam', 'bye-hello']
"""
words = input().split("-")  # input in one line

# words = input().split() # " " default: space
# print(words)

for word in words:

    print(f"------------- {word} ------------------------")
    if word.isdigit():
        print(f"I found a number! num: {word}")
    else:
        print("nothing!")

    if word.isupper():
        print(f"I found uppercase string! word: {word}")
    else:
        print("nothing!")

    if word.islower():
        print(f"I found lowercase string! word: {word}")
    else:
        print("nothing!")

    if word.isalnum():
        print(f"I found alnum string! word: {word}")
    else:
        print("nothing!")

    if word.startswith("h") and word.endswith("o"):  # startswith is case sensitive (حساس به حروف کوچگ و بزرگ)
        print("I guess I found hello")
    else:
        print("nothing!")

    print("-----------------------------------------")
