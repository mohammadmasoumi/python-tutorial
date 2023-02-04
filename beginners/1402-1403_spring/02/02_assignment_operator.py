# Assignment operator

"""
=
+=
-=
*=
/=
%=
**=

assign value to a variable
a = 12
"""

# WRITE [a] = READ [a] + 2
# NameError: name 'a' is not defined
# a = a + 2
# a += 2
# print(a)

# immutable
# تغییر ناپذیر                      
b = 2
b += 2
print(b)

b =+ 1 # WRONG
print(b)
b =- 1
print(b)

# b =* 2 # SYNTAX ERROR

# float + (float/int) = float
a = 12
a += 12 # 24
a -= 12 # 12
a /= 2 # 6.0 float
a *= 3 # 18.0
a //= 4 # 4.0
a **= 2 # 16.0
a %= 5 # 1.0
print(a)