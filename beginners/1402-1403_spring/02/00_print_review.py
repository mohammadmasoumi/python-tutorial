print("a", "b", "c")
print("a", "b", "c", sep="*")

# ["a", "b", "c"]
# SEP: "a*b*c"
# END:"a*b*c" + "*"
# "a*b*c*"
print("a", "b", "c", sep="*", end="*")
print("a", "b", "c", sep="*", end="")

# format specifier
# \n => next line
# \t => new tab
# \b => backspace
# \r => return carrage

# sep: " "
# end: "\n"

print("a\nb\nc", sep="*", end="*\n")
"""
a
b
c*

"""
print("a\n", "b\n", "c", sep="*", end="*\n")
"""
"a\n*b\n*c"
"a\n*b\n*c" + "*\n"
"a\n*b\n*c*\n"

a
*b
*c*

"""