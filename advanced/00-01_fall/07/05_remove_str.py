string = "hellofromhere"
a_list = list(string)

string = ''.join([item for item in a_list if item != 'e'])
string1 = ''.join([item for idx, item in enumerate(a_list) if idx != 5])

print(string)
print(string1)
print(type(string))

print("------------------")
# cast list to str

a = str(['a', 'b'])
a1 = "['a', 'b']"
print(a)
print(a[0], a[1], a[2])
print(type(a))
print(list(a))
print(list(a1))

print(list("hello from here"))
print(f'[{", ".join("hello from here".split())}]')
# for idx, char in enumerate(a_list):
#     # print(char, end='')
#     #  'str' object does not support item assignment
#     if item == 1:
#     a_list.remove()
