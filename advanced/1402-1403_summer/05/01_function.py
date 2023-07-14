# Function

def add(a, b):
    return a + b


# a, b?
# functions are variable

a = 10
b = a

# aliasing
# sum is alias of add
"""
ALIASING
python3 -m venv venv
pv

pv=aliase python3 -m venv venv
"""
sum = add

add(a, b)
sum(a, b)

"""
sum ------|
          v 
        [add]
          ^
add ------|
"""

print(add, type(add))
print(sum, type(sum))

print(id(add), id(sum))
