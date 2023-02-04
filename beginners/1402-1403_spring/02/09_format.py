# 1. 
# IndexError: Replacement index 1 out of range for positional args tuple
# print("hello {}, {}".format("ahmad")) # exception
print("hello {}, {}".format("ahmad", "mohammad"))
print("hello {}, {}".format("ahmad", "mohammad", "ali")) # ignore

# 2. 
name1 = 12
print("hello {name2}, {name1}".format(name1="ahmad", name2="mohammad"))
print("hello {a}, {b}".format(b="ahmad", a="mohammad"))
print("hello {a}, {b}, {b}".format(b="ahmad", a="mohammad"))
# KeyError: 'c'
# print("hello {a}, {b}, {c}".format(b="ahmad", a="mohammad"))

# 3.
print("hello {1}, {0}".format("ahmad", "mohammad"))
print("hello {1}, {0}, {0}".format("ahmad", "mohammad"))
# IndexError: Replacement index 2 out of range for positional args tuple
# print("hello {1}, {0}, {2}".format("ahmad", "mohammad"))

# 4. old version formatting
print("Hello %s %s" % ("ali", "hassan"))
print("%s %d" % ("ali", 12))
# TypeError: %d format: a real number is required, not str
# print("%s %d" % ("ali", "s"))
print("%s %i" % ("ali", 12))
print("%s %f" % ("ali", 12.2))