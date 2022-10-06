words = input().split()

# solution 1

# a = words[0]
# b = words[-1]
# c = words[1:-1]
#
# print(a, b, c)
# welcome to the club
# welcome ['to'] the club
# اول بقیه رو جایگرین میکند و سپس
# سراغ b میرود
a, *b, c, d = words

print(a, b, c, d)
