# tuple

# Changeable - mutable
# Ordered
# Duplication allowed
my_list = [1, 2 ,3 ,4, 1]
my_list.append(5)

# paranthesis
my_tuple1 = (1, 2, 3, 4, 1)
my_tuple2 = (1,)
my_tuple3 = (1) # redundant
#            0    1     2      3      4      5
my_tuple4 = (1, True, "ali", 19.2, [1, 2], (3, 4))

print(my_tuple1, type(my_tuple1))
print(my_tuple2, type(my_tuple2))
print(my_tuple3, type(my_tuple3))
print(my_tuple4, type(my_tuple4))

# access 
print(my_tuple4[4])
my_tuple4[4].append(3)
my_tuple4[4].extend([4, 5])
print(my_tuple4)

# TypeError: 'tuple' object does not support item assignment
# my_tuple4[1] = False

my_tuple5 = (1, True, "ali", 19.2, [1, 2], (3, [5, 6]))
print(my_tuple5[5])
print(my_tuple5[5][1])
my_tuple5[5][1].append(10)
print(my_tuple5)
