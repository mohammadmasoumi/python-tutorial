# enumrate
my_list = [1, 2, 3, 4]

# (0, 1) tuple

for item in enumerate(my_list):
    idx = item[0]
    elem = item[1]
    print(f"item: {item}, idx: {idx}, elem: {elem}")

print("-------------------")
for item in enumerate(my_list):
    idx, elem = item # unpacking
    # item: (0, 1)
    # idx, elem = (0, 1)
    print(f"item: {item}, idx: {idx}, elem: {elem}")

print("-------------------")
for idx, elem in enumerate(my_list):
    # idx, elem = (0, 1)
    print(f"idx: {idx}, elem: {elem}")

# # repeat action
# for _ in range(10):
#     print("Hello")

"""
Application:
    - update items in list, index

"""