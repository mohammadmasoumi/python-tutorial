list6 = [[[1, 2], [3, 4], [4, 5]], [[6, 7], [8, 9], [10, 11]]]

"""
list6 = [
    [[1, 2], [3, 4], [4, 5]], 
    [[6, 7], [8, 9], [10, 11]]
]
"""
print(list6)
print(list6[0], type(list6[0]))
print(list6[0][0], type(list6[0][0]))
print(list6[0][0][0], type(list6[0][0][0]))

a = f"{list6[0][0][0]}, {list6[0][0][1]}"
b = f"{list6[0][1][0]}, {list6[0][1][1]}"

print(a)
print(b)
print(a, b)
print(a, b, sep=", ")
