"""
Hhelloworld
H: 1
h: 1
e: 1
l: 2
o: 2
w: 1
d: 1
r: 1
...
"""
# [0:25] [26:51]
# [a-z] [A-Z]
#  a  b  c, ... . Z
# [0, 0, 0, ... , 0]
char_counts = [0] * 26 * 2
# lowercase character -> 97-123 -> [0:25]
# uppercase character -> 65-91 -> [26:52]

for character in input():
    ascii_code = ord(character)

    if ord('a') <= ascii_code <= ord('z'):
        idx = ascii_code - ord('a')
    elif ord('A') <= ascii_code <= ord('Z'):
        idx = ascii_code - ord('A') + 26

    char_counts[idx] += 1

for idx, value in enumerate(char_counts):
    if ord('a') - ord('a') <= idx <= ord('z') - ord('a'):
        character = chr(idx + ord('a'))
    elif ord('A') - ord('A') + 26 <= idx <= ord('Z') - ord('A') + 26:
        character = chr(idx - 26 + ord('A'))

    if value:
        print(f"{character}: {value}")
