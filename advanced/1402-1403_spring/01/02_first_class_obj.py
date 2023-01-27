# method 
# obj

# method
# function

# function
# add : function =  add(a, b): a + b
def add(a, b):
    return a + b

class A:
    # method
    def add(a, b):
        return a + b
    
# oop -> Object oriented programming
# functional programming
print(type(add))
# add = 2

# 12() callable
# TypeError: 'int' object is not callable
print(add("ali", "reza"))
print(add(12, 13))

# a = 12
# a = "hello"
# print(a + 12)

# alias
add2 = add
print(add)
print(add2)
print(add2(12, 13))
# fog
# f(add(12, 13))


# z = lambda x,y: add(x,y) and add2(x,y)
# d = {
#     "a": add,
#     "b": add2,
#     "c": add,
# }
# handler = d.get("a")
# handler()