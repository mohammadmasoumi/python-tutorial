def add(*asghar):
    # *asghar = 10, 12
    # asghar = (10, 12) 
    # 

    # [asghar] => [(10, 12)]
    # [*asghar] => [10, 12]

    return sum(asghar)

print(add(10, 12))


print("-------------------------")
print("-------------------------")
print("-------------------------")

# unpacking

# 1
a, b = 10 , 12
print(a, b)

# 2
# ValueError: not enough values to unpack (expected 3, got 2)
# a, b, c = 10 , 12
# print(a, b, c)

# 3
# ValueError: too many values to unpack (expected 2)
# a, b = 10, 12, 13
# print(a, b)

# 4
a, b = [12, 13]

# packing 
# 1.
# a = 10, b = 12, c = [13, 14, 15, 16]
a, b, *c = 10, 12, 13, 14, 15, 16
print(a, b, c)

# 2.
a, *b, c = 10, 12, 13, 14, 15, 16
print(a, b, c)

# 3.
*a, b, c = 10, 12, 13, 14, 15, 16
print(a, b, c)

# 4.
# SyntaxError: multiple starred expressions in assignment
# *a, *b, c = 10, 12, 13, 14, 15, 16
# print(a, b, c)

# 5.
a, b, *c = 10, 12
print(a, b, c)


