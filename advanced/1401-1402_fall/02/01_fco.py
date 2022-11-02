"""
return None

1. 
def add(a, b):
    print(a , b)

2. 
def add(a, b):
    print(a , b)
    return None

3.
def add(a, b):
    print(a , b)
    return 
"""

"""
function application

1. reusable
2. break down the logic
"""

# variable
# name: add
# type: function
# value: function signature
def add(a, b):
    # a = 10, b = 12
    c = a + b # c: 22
    print(c) # print 22 in terminal
    # return None

# call/invoke 
# input: 10, 12
d = add(10, 12) # None
# d: None
print(d)
# print(add(10, 12))
# ------------------
# print None in terminal
# 22
# None
print("-------------------------")

def shout():
    print("Hello")
    # return None

print(shout)   # function shout at #AB12
# print(None) # None
print(shout()) # Hello
print("-------------------------")

yell1 = shout 
yell2 = shout() # Hello

print(yell1) # <function shout at 0x000001CD7A4D00D0>
print(yell2) # None