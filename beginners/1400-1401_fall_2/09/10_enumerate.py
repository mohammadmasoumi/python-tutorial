# range
# enumerate


my_list = ["apple", "apricot", "watermelon", "orange"]

# unpacking

# a, b = 12, 13
# c, d = [12, 13]

# (index, item)
for elem in enumerate(my_list):
    # (0, 'apple'), (1, 'apricot'), (2, 'watermelon'), (2, 'watermelon')
    index, item = elem
    print(f"index: {index}, item: {item}, elem: {elem}")

print("------------------------")
for index, item in enumerate(my_list):
    print(f"index: {index}, item: {item}")
