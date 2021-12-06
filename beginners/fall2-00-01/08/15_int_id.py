
# cache int values between -5, 255
# the same box

"""
a and b point to the same box
    a =>     __________
             |    12   |
    b =>     __________


   ------------------------------------------
    a !=>     __________
             |    12   |
    b =>     __________

    a =>     __________
             |    13   |
             __________
"""

a = 12
b = a

print(id(a), id(b))
# a = 13 => create new box , immutable
a = 13
print(id(a), id(b))


#
a1 = 300
b1 = a1
print(id(a1), id(b1))
