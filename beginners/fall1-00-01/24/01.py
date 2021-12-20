# Q1
text = input()

characters = {}

for char in text:

    if characters.get(char):
        characters[char] += 1
    else:
        characters[char] = 1


for char, count in characters.items():
    print(f"{char}: {count:>5}")
