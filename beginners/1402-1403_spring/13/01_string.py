# join()	Converts the elements of an iterable into a string
#               iterable
print("&".join(["hello", "world"]))

# 102030405
my_list = [1, 2, 3, 4, 5]

# TypeError: sequence item 0: expected str instance, int found

# print(str(my_list))
print(str(my_list))

# "[1, 2, 3, 4, 5]"
#
# for char in  "[1, 2, 3, 4, 5]":
#     print(char)
print("0".join(str(my_list)))  # [010,0 020,0 ...
print("|".join("hello"))
print("0".join([str(item) for item in my_list]))
print("0".join(map(lambda x: str(x), my_list)))
