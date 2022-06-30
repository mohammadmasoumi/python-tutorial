

"""
function
  - name
  - (0 or OO)inputs, params
  - (1 or OO)output

keyword: def

sample: 
    def add(a, b):
        return a + b

usage:
  - reusability
  - separation of logic

"""

def add(a, b):
    # a, b params
    # code block
    return a + b

def complicated_operation(a, b):
    # a = 12, b = 13
    a = a + b
    b = a + b
    return a * b * 10

# ----------------------------------
print(12 + 13)
# invoke, call
print(add(12, 13)) # args
c = add(12, 13)
# c = 25
print(             add(12, 13)          ) # args
# print(             25          ) # args

# -----------------------------------
print(complicated_operation(10, 12))
print(complicated_operation(11, 12))
# -----------------------------------
a = 10
b = 12
a = a + b
b = a + b
print(a * b * 10)
# -----------------------------------
a = 11
b = 12
a = a + b
b = a + b
print(a * b * 10)
# -----------------------------------

# move
#  - right
#  - left
#  - north
#  - south