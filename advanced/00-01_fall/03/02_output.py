
a = 12
b = 2

# f-string
print(f"a is: {a} b is: {b}")

# format
print("a is: {} b is: {}".format(a, b))
print("a is: " + str(a) + " b is: " + str(b))


# print
# def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
print(a, b, a, b, sep="-", end="EOF")
print(a, b, a, b, sep="-", end="EOF\n")
print("ali\n")
print("ali")