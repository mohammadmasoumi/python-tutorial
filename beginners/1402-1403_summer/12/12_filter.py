# map(function, iterable) 
# result <- function(each item in iterable)

# filter(function, iterable)
# result <-  True :function(each item in iterable)

my_list = [1, 2, 3, 4, 5]

# filter
print(list(filter( lambda x: x%2 == 0, my_list)))

#                       1%2 -> 1 -> bool(1) -> True
print(list(filter( lambda x: x%2, my_list)))


a = 13
if 1: # bool(a)
    print("Hello")

if a % 2: # a % 2 = 1
    print("hello")

# map
# [1, 2, 3, 4, 5]
#       ||
#       V   
# -> lambda x: x%2 ->
#       ||
#       V
# [1, 0, 1, 0, 1]
print(list(map( lambda x: x%2, my_list)))
print(list(map( lambda x: x*2, my_list)))
print(list(map( lambda x: bool(x%2), my_list)))
