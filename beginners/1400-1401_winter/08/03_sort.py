my_list = [1, 0, 50, 49, 7, 51, 60]

# ?
# | x - 50|
# [50, 51, 49, 60, 7, 1, 0]
# variable.(function)
print(my_list.sort())
print(my_list) # ASC 

my_list.sort(reverse=True) # DSC
print(my_list)

def my_function(item):
    return abs(item - 50)

my_list.sort(key=my_function) 
print(my_list)


