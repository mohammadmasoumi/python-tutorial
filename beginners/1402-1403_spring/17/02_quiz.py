
my_list = [1, 2, 3, 4, 5]

iterator = iter(my_list)

print(next(iterator)) # 1
print(next(iterator)) # 2
print(next(iterator)) # 3

for item in iterator: # next(iterator)
    # 4
    print(item)
    break

# StopIteration
print(next(iterator)) # 5