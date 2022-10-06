# if condition


"""

if - selection statement

True => do this
False => do that

Signature
if - keyword

indentation
if condition:
    # code block
    execute this block if condition is satisfied/true
    #
    #
    #
    #
    #

# the rest of code
------------------------------
condition: int
if condition:
if 12:

if bool(12):
    print("Hello")

------------------------------
a = 12
if a == 12: if a is equal to 12
if a: if a is not zero if bool(a)
------------------------------
"""

a = 12

if a == 12:
    print("a is 12!")

if a:  # bool(a) => True, False
    print("a is not zero")

c = 0
# if c:  # bool(0) => False
if c:  # bool(0) => False
    print("zero")

if False:
    print("False")

#
if True:
    print("True")

print("True")

#
if 1:  # bool(a) => True
    print("Bye")
