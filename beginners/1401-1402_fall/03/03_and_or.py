# and or - condition operator

condition1 = "Hello"
condition2 = 12
condition3 = 0

#       "Hello"         12
# bool("Hello")
print(bool(condition1) and condition2) # condition2
print("" and condition2) # ""
print(condition2 or condition3) # 12
print(condition3 or condition2) # 12


# print(bool(0) and 12/0)
print(0 and bool(12) and 12/0)

# if 0 != 0:
#     print(12/0)

a = 12
b = 0

if (b != 0):
    print(a /b)

print(b and a/b)


# bool(b) => a/b
# bool(a/b)
if bool(b and a /b):
    print()


