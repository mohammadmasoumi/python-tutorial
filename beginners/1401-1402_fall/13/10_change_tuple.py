tuple1 = (1, 2, 3)
# re-assignment
tuple1 += (4,)

a = 12
a += 1

print(tuple1)
print("----------------")
# TypeError: can only concatenate tuple (not "int") to tuple
# tuple1 = (1, 2, 3)
# # re-assignment
# tuple1 += (4) # redundant paranthesis

# print(tupel1)
# TypeError: unsupported operand type(s) for -=: 'tuple' and 'tuple'
# tuple1 -= (4, )
# print(tuple1)