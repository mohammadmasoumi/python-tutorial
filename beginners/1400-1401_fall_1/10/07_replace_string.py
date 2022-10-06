# s = input()
#
# # ["5", "k"]
# # "5 k"
#
# # "5 k".split()
# # ["5", "k"]
# # a, b = ["5", "k"]
# # a = "5"
# # b = "k"
#
# index, replace_character = input().split()
#
# print(s[0])
# print(s[0:2])
# print(s[:int(index)], s[int(index):])
#
r = "k"
s = "asghar"
# "asgh" + "k" +  "r"
# "asghkr"

a = "Hello"
b = "World"
# print(a[2:] + "a" + b[2:])

# print(s[0])
# print(s[:2])
# print(s[2:])
# print(s[:2] + s[2:])
# print(s[2:] + s[:2])

index = 5
char = "-"
#    01234 5 678910
c = "Hello world"

print(c[:index])
print(char)
print(c[index + 1:])
print(c[:index] + char + c[index + 1:])
