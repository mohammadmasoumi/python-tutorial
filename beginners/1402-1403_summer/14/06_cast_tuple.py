# cast

t1 = (1, 2, 3)

# tuple
print(tuple(t1))

#                  012345678
print(str(t1))  # "(1, 2, 3)"
print(str(t1)[8])
print("----------------")
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
# print(int(t1))
# print(float(t1))

empty_tuple = tuple()
print(bool(t1))
print(bool(empty_tuple))

print("----------------")
print(list(t1))

my_list = list(t1)
my_list.append(4)
t1 = tuple(my_list)
print(t1)

# 
# my_list.count()
