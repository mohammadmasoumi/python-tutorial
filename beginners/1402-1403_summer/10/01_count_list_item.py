"""
my_list = ["a", "b", "a", "c", "x", "y"]

item = "a"
"a" -> 0
result[0] += 1

lower_case alphabetic

a: 2
b: 1
c: 1
d: 0
...

"a" -> 0
"b" -> 1
"c" -> 2
...
"z" -> 25


# result
 0             25 
[2, 1, 1, 0, ..., 1]
 a, b, c, d, ..., x

"""
my_list = ["a", "b", "a", "c", "x", "y"]

#  0  1  2  3  4 ...
# [0, 1, 2, 1, 2, 3, 0, .., 2]
result = [0] * 26 # [0, 0, 0, ..., 0] 
# ["a"] * 2 => ["a", "a"]

# result: []
# "z" -> 25
# result[25] => index out of range

#              ord index
# ord("a") -> 97 -> 0
# ord("b") -> 98 -> 1
# ....

# [97, ..., 123] => [0, 1, ..., 25]
# -97 -> ord("a")

# ord(item) - ord("a")

for char in my_list:
    # index on result
    index = ord(char) - ord("a")
    result[index] += 1

print(result)

c = input()
print(result[ord(c) - ord("a")])
