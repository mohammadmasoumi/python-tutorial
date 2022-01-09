#   start end(not included) step
print(range(1, 10, 2))
print(list(range(1, 10, 2)))
print(list(range(100, 10, -2)))

# Generating index
my_list = [1, 2, 3, 4, 5]

for idx in range(len(my_list)):
    print(f"idx: {idx}")
