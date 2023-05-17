my_list = [1, 2, 3, 4, 5]

iterator = iter(my_list)

print(next(iterator)) # 1

# iterable -> iterator
# iterator 
for item in iterator:
    # item: next(iterator) 
    if item > 2:
        break
    
    # StopIteration

# item: 3 break

print(next(iterator)) # 4

