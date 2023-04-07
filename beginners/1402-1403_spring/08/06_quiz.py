fruits = ["lemon", "orange", "apple", "lemon", "orange"]

# ["orange", "lemon", "apple", "orage", "lemon"]

# print(fruits[::-1])

# idx = 0

# for fruit in fruits:
#     if fruit == "lemon":
#         fruits[idx] = "orange"
#     elif fruit == "orange":
#         fruits[idx] = "lemon"
    
#     idx += 1

# print(fruits)

idx = 0
lemon_idx = 0

for fruit in fruits:
    if fruit == "lemon":
        lemon_idx = idx
    elif fruit == "orange":
        # swap, replace
        # a, b= b, a
        fruits[lemon_idx], fruits[idx] = fruits[idx], fruits[lemon_idx]

    idx += 1

print(fruits)