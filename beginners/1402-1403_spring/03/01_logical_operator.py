# logical operator

"""
python java
and     && 
or      ||
not     !

operator: *
operand: 1, 2

AND - binary operator
----------------
| C1 | C2 | Res|
----------------
|  T |  T |  T |
----------------
|  F |  F |  F |
----------------
|  T |  F |  F |
----------------
|  F |  T |  F |
----------------
Example: c1 and c2

OR - binary operator
----------------
| C1 | C2 | Res|
----------------
|  T |  T |  T |
----------------
|  F |  F |  F |
----------------
|  T |  F |  T |
----------------
|  F |  T |  T |
----------------
Example: c1 or c2

NOT - unary operator
-----------
| C1 | Res|
-----------
|  T |  F |
-----------
|  F |  T |
-----------

Example: not c1

# Note

[AND]
> condition1 and condition2
if condition1 is False, I won't check condition2 

[OR]
if condition1 is True, I won't check condition2 


a = 12
b = 0

if b!=0 and a/b==2:

if a/b==2 and b!=0:
    
Can't divide by zero
"""

a = 12
b = 0

# syntax exception/error
# f b!= 0:

# if b!=0 and a/b==2:
#     print("Hello")

# if a/b==2 and b!=0:
#     # Logical exception/error
#     # ZeroDivisionError: division by zero
#     # Exit
#     print("Bye")

print("Good morning")

# if b != 0:
#     c = a/b
# else:
#     c = False

c = b != 0 and a/b
print(c)

b = 1
c = b != 0 and a//b
print(c)

c = b != 0 and a/b
print(c)

c = b!=0 and a!=0 and a/b
print(c)

c = b!=0 and a!=0 and a/b==2
print(c) # True or False: result of `a/b==2` expression




