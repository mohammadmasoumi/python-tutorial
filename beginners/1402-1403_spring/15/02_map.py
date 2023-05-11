my_list = [1, 2, 3, 4]

# update elements of list

# lambda input:ouput
print(list(map(lambda a:a*2, my_list)))

# filter
print(list(filter(lambda a:a%2, my_list)))