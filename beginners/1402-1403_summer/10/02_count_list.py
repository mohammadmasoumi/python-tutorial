"""

my_list = ["a", "b", "A", "B", "a", "c"]

result: 52
0      25 26      51
a, .., z, A, ..., Z
[]
"""

my_list = ["@", "b", "A", "B", "a", "c"]

# [0] * 52
# [0, 0, ..., 0]
# ["A"] * 52
# ["A", "A", "A", ..,"A"]
#         0 
result = [0] * 52


"""

0,           51
[            ]

lowercase  uppercase
0, 25      26, 51
[]         []

a: 2 -> 0
A: a -> 26

97, ..., 123 -> 0, ..., 25
65, ..., 81 -> 26, ..., 51
"""

for char in my_list:
    # [0, 25] lowercase
    # char
    # lowercase or uppercase ???
    # "@"
    if ord("a") <= ord(char) <= ord("z"):
        index = ord(char) - ord("a")
        result[index] += 1

    # [26, 51] uppercase
    elif ord("A") <= ord(char) <= ord("Z"):
        index = ord(char) - ord("A") + 26
        result[index] += 1

    # @ => index: undefined ??
    # NameError: name 'index' is not defined
    # result[index] += 1

print(result)