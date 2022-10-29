# ValueError: invalid literal for int() with base 10: '12 13 14'
# raw_items = int(input())
raw_items = input() # str
items = raw_items.split("+") #

# ["12", "13", "14"]
print(items, type(items))

# cast all items to int
#   0      1    2
# ["12", "13", "14"]
# [(0, "12"), (1, "13"), (2, "14")]
# for item in enumerate(items):
#     # (0, "12")
#     # a, b = 12, 13
#     # a, b = [12, 13]
#     a, b = item
#     index, elem = item

# for index, elem  in enumerate(items):
#     print(index, elem)


for index, item in enumerate(items):
    print(f"index: {index} | item: {item}")
    items[index] = int(item)

print(raw_items, type(raw_items))
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
# print(int(items), type(items))