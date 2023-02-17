# method on list

my_list = [1, 2, 3, 4, 5, 6]


"""
function

(x,y, ...) => [f] => (x1,y, ...)

f(x)=x^2
f(2)=4
f(3)=9
f(4)=16

def function_name(inputs):
    return outputs

"""

# append: add element to the end of list

# inputs: 7
# output: None
my_list.append(7)
# TypeError: list.append() takes exactly one argument (2 given)
# my_list.append(8, 9)
# my_list.append(8)
# my_list.append(9)
#  0                 6
# [1, 2, 3, 4, 5, 6, 7]
print(my_list)
# IndexError: list assignment index out of range
# my_list[7] = 8

my_list = my_list.append(7)
print(my_list)

"""
my_list = [1, 2, 3, 4, 5, 6]

def append(value):
    # my_list = my_list + [value]
    # [1, 2, 3, 4, 5, 6, 7]
    my_list += [value]
    return None

a = append(7)
print(my_list) #  [1, 2, 3, 4, 5, 6, 7]
print(a) # None
my_list = append(8)
print(my_list) # None
"""

# extend
my_list = [1, 2, 3, 4, 5, 6]
# iterable: for loop
my_list.extend([7, 8, 9])
# TypeError: list.extend() takes exactly one argument (2 given)
# my_list.extend([7, 8, 9], [7, 8, 9])
my_list.append([7, 8, 9])

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, [7, 8, 9]]
print(my_list)

my_list.extend("hello")
print(my_list)

my_list.append("hello")
print(my_list)

# insert

my_list = [1, 2, 3, 4, 5, 6]
#            index item
my_list.insert(0, 10)
my_list.insert(0, [10, 11, 12])
my_list.insert(0, (10, 11, 12))
# [10, 1, 2, 3, 4, 5, 6]
print(my_list)

my_list = [1, 2, 3, 4, 5, 6]
my_list.insert(1, 10)
# [1, 10, 2, 3, 4, 5, 6]
print(my_list)

# insert as append
my_list.insert(7, 10)
print(my_list)
my_list.insert(10, 10)
print(my_list)
my_list.insert(-1, 10)
print(my_list)
my_list.insert(-20, 10)
print(my_list)

my_list = [1, 2, 3, 4, 5, 6]

my_list.insert(10, 10)
print(my_list)

my_list.insert(9, 100)
print(my_list)

# TypeError: 'list' object cannot be interpreted as an integer
# my_list.insert([9], 100)
# print(my_list)

# pop index
my_list = [1, 2, 3, 4, 5, 6]

my_list.pop()  # 6
print(my_list.pop())  # 5
item = my_list.pop()  # item: 4
print(my_list)  # [1, 2, 3]
print(item)  # 4

# index
my_list = [1, 2, 3, 4, 5, 6]

item = my_list.pop(0)
print(my_list, item)

item = my_list.pop(-1)
print(my_list, item)

index = -2
item = my_list.pop(index)
print(my_list, item)

# IndexError: pop index out of range
# item = my_list.pop(10)
# print(my_list, item)

# remove item
my_list = [10, 20, 30, 40, 50, 60]

# ValueError: list.remove(x): x not in list
#               item
# my_list.remove(0)

item = my_list.remove(10)
print(my_list, item)

# del my_list[0]
my_list = [10, 20, 30, 40, 50, 60, 10]
# remove first 10 from left
my_list.remove(10)  # [20, 30, 40, 50, 60, 10]
print(my_list)

# TypeError: list.remove() takes exactly one argument (2 given)
# my_list.remove(10, 20)

# count
my_list = [10, 20, 30, 40, 50, 60, 10]

print(my_list.count(10))
print(my_list.count(100)) # 0

# clear
my_list = [10, 20, 30, 40, 50, 60, 10]
my_list.clear()

print(my_list)
 

