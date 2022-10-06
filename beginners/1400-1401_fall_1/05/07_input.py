# get input
# default space
# a = input()
# b = input().split()
# c = input().split('-')
# b = input()

# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# print(b, type(b))

b = input().split()
print(b, type(b))

# a_string = "12"
# print(int(a_string), type(int(a_string)))
# print(a_string, type(a_string))
# a_string = int(a_string)

for idx, item in enumerate(b):
    # print(item, type(item))
    print(item, type(item))
    # update element
    # item = int(item)
    b[idx] = int(item)
