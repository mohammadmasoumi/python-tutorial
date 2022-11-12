# hello world hello world
# 26 characters

# heLlo@worlD$hEllo#World^>1029

words = input().lower().replace(" ", "")

"""
character  index
a           0
b           1
c           2
d           3
...         ...

letters_count = [0] * 26

 a  b       z
[0, 0, ..., 0]

ascii code
    ord     -97
a   => 97   => 0
b   => 98   => 1
...
z   => 122  => 25
"""
letters_count = [0] * 26

for character in words:

    # if character == "a":
    #     letters_count[0] += 1
    # elif character == "b":
    #     letters_count[1] += 1
    # ...
    # if character != " ":
    index = ord(character) - 97
    letters_count[index] += 1

#                 0  1  2
#                 a  b  c
# letters_count: [0, 1, 2, 0, 3, ..., 0]
for index, count in enumerate(letters_count):
    if count > 0:
        character = chr(index + 97)
        print(f"{character}: {count}")
