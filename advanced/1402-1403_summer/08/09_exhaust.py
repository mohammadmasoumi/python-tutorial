my_list = [1, 2, 3, 4, 5, 6]

# iterator save state
iterator = iter(my_list)

print(next(iterator)) # 1
print(next(iterator)) # 2
print(next(iterator)) # 3

# iterable -> iterator
# iterator 

for item in iterator:
    # next(iterator)
    # item: 4
    # item: 5
    # item: 6
    # StopIteration
    print(f"Hello {item}")

for item in iterator:
    # next(iterator)
    # StopIteration
    print(f"Hello {item}")

# iterator: iter(my_list)
for item in my_list:
    print(item)

# create new iterator
# iterator: iter(my_list)
for item in my_list:
    print(item)