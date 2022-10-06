a_list = [1, 2]

a1 = a_list[0]
b1 = a_list[1]

print(a1, a_list[0])
print(b1, a_list[1])
# print(a_list[2]) # IndexError: list index out of range

# ---------------------------- 1 ----------------------------
a2, b2 = a_list
print(a2, b2)
print("-------------------")
# ---------------------------- 2 ----------------------------

# ValueError: too many values to unpack (expected 2)
# a3, b3 = [1, 2, 3]
# print(a3, b3)
print("-------------------")

# ---------------------------- 3 ----------------------------
# ValueError: not enough values to unpack (expected 3, got 2)
# a4, b4, c4 = [1, 2]
# print(a4, b4, c4)
# print("-------------------")

# ---------------------------- 4 ----------------------------
# ValueError: too many values to unpack (expected 2)
a5, *b5 = [1, 2, 3]
print(a5, b5)

a6, *b6, c6 = [1, 2, 3, 4]
print(a6, b6, c6)
