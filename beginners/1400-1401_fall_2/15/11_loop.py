my_tuple = (12, 13)

for item in my_tuple:
    print(item)

print("-------------------------")
for idx, item in enumerate(my_tuple):
    print(idx, item)

print("-------------------------")
for idx in range(len(my_tuple)):
    print(idx, my_tuple[idx])

#          start, end(not included), step
print(list(range(10, 100, 10)))
