"""
helloworld
h: 1
e: 1
l: 2
o: 2
w: 1
d: 1
r: 1
...
"""
# [0, 0, 0, .., 0]
char_counts = [0] * 26

# 20 -> m
# print(char_counts[19])

# ord, chr
# ord('a') => ascii code
# chr(97) => character

for character in input():
    # idx ???
    # character ==> index
    idx = ord(character) - ord('a')
    # char_counts[idx] = char_counts[idx] + 1 
    char_counts[idx] += 1

# char_counts
#  0  1  2  3  4 ...
#  a  b  c  d  e ... 
# [1, 0, 1, 2, 0, 0, ..., 0]
"""
h: 1
e: 1
l: 2
o: 2
w: 1
d: 1
r: 1
"""
for idx, value in enumerate(char_counts):
    # index ==> character
    character = chr(idx + ord('a'))
    # value != 0
    # value: 1 => bool(1) = True
    # value: 0 => bool(0) = False
    if value:
        print(f"{character}: {value}")
