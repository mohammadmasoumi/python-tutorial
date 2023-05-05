# list comprehension

"""
application: 
filter and update all elements of a list

- create new list

- COPY
list: []
copied_list: [item for item in list]
double_list: [item*2 for item in list]
even_list: [item for item in list if item%2==0]
double_even_list: [item*2 for item in list if item%2==0]

"""

my_list = [1, 2, 3, 4, 5]

copied_list = [item for item in my_list]
double_list = [item*2 for item in my_list]
even_list = [item for item in my_list if item % 2 == 0]
double_even_list = [item*2 for item in my_list if item % 2 == 0]
odd_list = [item for item in my_list if item % 2]  # item%2 => 1

# [ TRUE_VALUE if CONDITION else FALSE_VALUE for ITEM in ITEMS]

odd_even_list = [item * 2 if item % 2 else item // 2 for item in my_list]

#  if item%2 => if bool(item%2)
# bool(item%2)
#   item%2 => 0 => bool(0) => False
#   item%2 => 1 => bool(1) => True

print("-----------------------------")
print(
    f"copied_list: {copied_list}, id_copied_mylist:{id(copied_list)}, id_mylist:{id(my_list)}")
print(f"double_list: {double_list}")
print(f"even_list: {even_list}")
print(f"double_even_list: {double_even_list}")
print("-----------------------------")

my_list = [1, 2, 3, 4, 5]

# [item > 0 for item in my_list]
# [True, True, True, True, True]
# all([True, True, True, True, True])
# => True

if all([item > 0 for item in my_list]):
    print("All elements are greater than zero")

my_list = [-1, 0, 3, 4, 5]
greater_than_zero = [item for item in my_list if item > 0]
print("-----------------------------")

my_list = [[1, 2], [3, 4], [5, 6], [7, 8]]
# flatten list
# 2D => []
# [1, 2, 3, 4, 5, 6, 7, 8]

flatten_list = [item for items in my_list for item in items]
flatten_even_list = [
    item for items in my_list for item in items if item % 2 == 0]

flatten_odd_list = [
    item for items in my_list for item in items if item % 2]

flatten_even_odd_list = [item * 2 if item %
                         2 else item // 2 for items in my_list for item in items]


"""
Pythonista

1. update all elements
    [item* 2 for item in my_list]
    [str(item) for item in my_list]
    [item>2 for item in my_list]
    
    [100, 200, 300, 400]
    [100100, 200200, 300300, 400400] "100" * 2 = "100100" (int)=> 100100
    [int(str(item)* 2) for item in my_list]
    [int(str(item)* 2) if item == 200 else item for item in my_list]
    "".join([str(item)* 2 for item in my_list]) => 100100200200300300400400

2. filter all elements
    [item for item in my_list if item%2==0]
    [item for item in my_list if item%2]
    [item for item in my_list if item<0]
    # my_list[2:]
    [item for idx, item in enumerate(my_list) if idx>1]
    
3. filter and update all elements
    [item*2 for item in my_list if item%2==0]
    [item//2 if item%2==0 else item*2 for item in my_list]


# come together
join str
all
any
list comprehension
"""

print(flatten_list)
print(flatten_even_list)
print(flatten_odd_list)
print(flatten_even_odd_list)

my_list = [1, 2, 3, 4]
print([item * (idx+1) for idx, item in enumerate(my_list)])

my_list = [100, 200, 300, 400]
print([int(str(item) * (idx+1)) for idx, item in enumerate(my_list)])

names = ["asghar", "akbar", "ali", "mohammad", "hasan"]

print("-".join([name for name in names if name.startswith('a')]))

n = "ali-asghar-akbar"
# "aliali-asgharasghar-akbarakbar"

# ["ali", "asghar", "akbar"]
print("-".join([name * 2 for name in n.split("-")]))
