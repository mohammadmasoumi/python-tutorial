# string
my_list = ["apple", "orange"]
my_list.extend("banana") # iterable
print(my_list)
print(len(my_list))

# str 
# get characters of string with index
#            012345678910
my_string = "hello world"
print(my_string[0])
print(my_string[5])
print(my_string[6:])
print(my_string[-5:])

# update
my_list[0] = "orange"
print(my_list)

# TypeError: 'str' object does not support item assignment
# my_string[0] = "M"
# re-assignemnt
my_string = "M" + my_string[1:]
print(my_string)
print(len(my_string))
