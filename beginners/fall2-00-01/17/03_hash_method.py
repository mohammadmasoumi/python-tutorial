

def cutome_hash(item):

    # type(item) == int
    if isinstance(item, int):
        return item
    elif isinstance(item, str):
        sum = 1
        for char in item:
            sum *= ord(char)
        return sum
    elif isinstance(item, float):
        return item * 100

    # return None

print(cutome_hash(12))
print(cutome_hash(12.2))
print(cutome_hash("ali"))
print(cutome_hash("ali"))
print(cutome_hash("asghar"))

# test
print("-------------------------")
print({1, 2, True})
print({True, 2, 1})