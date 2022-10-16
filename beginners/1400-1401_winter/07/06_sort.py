# sort
my_list = [1, 50, 7, 20 , 49]


# method / function
# f(x) = x ^ 2
# vorudi: x
# khoruji: x ^ 2
def custom_sort(item):
    return abs(item - 50)

# default value of reverse is False
# reverse is optional 
# my_list.sort(key=custom_sort)
my_list.sort(key=custom_sort, reverse=True)
print(my_list)