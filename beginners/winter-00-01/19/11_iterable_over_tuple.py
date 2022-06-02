my_tuple = (1, 2, 3)

for item in my_tuple:
    print(item)

print("----------------------")
for idx in range(len(my_tuple)):
    print(my_tuple[idx])

print("----------------------")
for idx, item in enumerate(my_tuple):
    print(idx, item)

print("----------------------")
for item in enumerate(my_tuple):
    print(item, type(item))