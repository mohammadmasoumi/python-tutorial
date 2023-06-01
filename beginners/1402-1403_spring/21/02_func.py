# pass by reference 
# pass by value

# m1 = [1, 2, 3]
# m2 = m1 # same refence 
# m2.append(4)
"""
mutable
m1 -> [1, 2, 3, 4] <- m2
"""

# m1 = "ali"
# m2 = m1
# m2 = "reza"
"""
immutable
m1 -> "ali" </- m2
m2 ->  "reza"
""" 

# pass by assignment
# pass by object reference
def do_sth(a: str, b: list):
    # a = in1
    # b = in2
    a = "new  ali"
    print(f"a: {a}")

    b.append("amir")
    print(f"b: {b}")


in1 = "ali" # pass by value
in2 = ["reza"] # pass by reference
do_sth(in1, in2)

print(f"in1: {in1}")
print(f"in2: {in2}")