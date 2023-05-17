
# map filter

my_list = [1, 2, 3, 4]

iterator = map(lambda x: x*2, my_list)

# <map object at 0x0000024AD155AA40>
print(iterator)
# print(list(iterator)) # exhausted 
# StopIteration
print(next(iterator))
print(next(iterator))
