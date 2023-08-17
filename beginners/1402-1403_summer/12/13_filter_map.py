# filter, map

my_list = [1, 2, 3, 4, 5]

# map: [2, 4, 6, 8, 10]
# filter: []
# [] 
#                       bool(x%2) -> True Odd
print(list(filter(lambda x: x%2, map(lambda x: x*2, my_list))))
print(list(filter(lambda x: x%2, map(lambda x: x*3, my_list))))

# filter: [1, 2, 3, 4, 5]  X [2, 4, 6, 8, 10]
# map: [1, 0, 1, 0, 1]    
print(list(map(lambda x: x%2, filter(lambda x: x*2, my_list))))
print(list(map(lambda x: x%2, filter(lambda x: x%2, my_list))))