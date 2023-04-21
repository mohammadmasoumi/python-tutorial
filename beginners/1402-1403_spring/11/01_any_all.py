# any all

my_list = [1, 2, 3, 4]

#   type    truthy  falsy
#   str             ""
#   int             0
#   float           0.0
#   list            []
#   bool            False


# bool(0) => false
"""
a = 0

if a: # bool(a) => False
    print("Hello")

"""

# all variables are truthy => True
print(all(my_list)) # True
print(all([0, 1, 1, 1])) # False

# any variables are truthy => True
# at least one variable is truthy => True
print(any([0, 0 , 0 , 1])) # True
print(any([0, 0 , 0 , ""])) # False

# ----------------------
my_list = [1, 2, 3, 4]

print(all(map(lambda x: x>0, my_list))) # True