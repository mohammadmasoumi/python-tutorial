
my_list = [[1, 2], [3, 4], [5, 6]]

for idx, item in enumerate(my_list):
    # idx:0, item:[1, 2]
    # idx:1, item:[3,4]
    print(idx, item)

print("----------------------")
for idx, (a, b) in enumerate(my_list):
    # idx, item
    # 0, [1, 2]
    # idx, a, b = 0, [1, 2]

    print(idx, a, b)

# ValueError: not enough values to unpack (expected 3, got 2)
# idx, (a, b) = 0, [1, 2]
# print(idx, a, b)
# idx, (a, b) = 0, [1, 2]
# print(idx, a, b)

# Happy
# idx, (a, b) = 0, [1, 2]