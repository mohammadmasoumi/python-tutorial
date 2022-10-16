my_tuple = (1, 2, 3)

# re-assign
# my_tuple = my_tuple + (4, 5)
a = 12
a += 2
my_tuple += (4, 5) # Yes/No 

print(my_tuple)
print(my_tuple * 2)
print(a)

# -------------
my_tuple1 = (1, 2, 3)
my_tuple2 = (1, 2, 3)
print(my_tuple1 + my_tuple2)
my_tuple1 = my_tuple1 + my_tuple2
print(my_tuple1)

# it does not change the original tuple
print(tuple(map(lambda x: x * 2, my_tuple))) # a new tuple 
print(my_tuple)