string = "helloworldhowareyoudoing"

"""
 0  1  2  3       25
 a  b  c  d       z
[0, 2, 1, 0, ..., 0] # [0] * 26

f("a") -> 0
f("b") -> 1
....
f("z") -> 25

         -97
[97, 123] => [0, 25]

ord("a") -> 97 -> ord("a") - ord("a") => 0
ord("b") -> 98 -> ord("b") - ord("a") => 1
...
ord("d") -> 100 -> ord("d") - ord("a") => 3
"""
char_counts = [0] * 26

for char in string:
    idx = ord(char) - ord("a")
    char_counts[idx] += 1

# print(char_counts)
for idx, count in enumerate(char_counts):
    char = chr(idx + ord("a"))
    print(f"{char}: {count}")

# max occurance
# value = max(char_counts)
# idx = char_counts.index(value)
# print(chr(idx + 97))