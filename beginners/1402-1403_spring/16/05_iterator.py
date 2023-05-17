my_list = [1, 2, 3, 4, 5]

iterator = iter(my_list)

print(next(iterator)) # 1

# iterable -> iterator
# iterator 

# new_iterator: iter(my_list) 
for item in my_list:
    # item: next(new_iterator) 
    if item > 2:
        break

print(next(iterator)) # 2

