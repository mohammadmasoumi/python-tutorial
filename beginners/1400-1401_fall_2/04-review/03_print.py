"""
*args, sep=' ', end='\n', file=None

if you dont give `sep` => it will use default value.

default value
override
"""

# sep
print("hello", "world", "a", "b")  # sep => space
print("hello", "world", "a", "b", sep="-")  # sep => -
print("hello", "world", "a", "b", sep="***")  # sep => -, end=\n

# end
# \n next line
# print("hello", "world", "a", "b", end="\n")
print("hello", "world", "a", "b", end="**\n")
print("hello", "world", "a", "b", end="**")
print("hello", "world", "a", "b", end="")
