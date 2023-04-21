my_list = [[1, 2], [3, 4]]

for idx, items in enumerate(my_list):
    print(idx, items)

for item1, item2 in my_list:
    print(f"item1: {item1}, item2: {item2}")

print("------------------------")
# ValueError: too many values to unpack (expected 2)
# my_list = [[1, 2], [3, 4, 5]]
# for item1, item2 in my_list:
#     print(f"item1: {item1}, item2: {item2}")

# my_list = [1, 2, 3, 4, 5]
# item1, item2 = 1
# TypeError: cannot unpack non-iterable int object
# for item1, item2 in my_list:
#     print(f"item1: {item1}, item2: {item2}")
