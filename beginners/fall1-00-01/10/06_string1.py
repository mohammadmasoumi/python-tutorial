# count
c = "abcdefabcdef"

print(c.count("a"))
print(c.count("k"))

# replace

c = "Hello world"
# print(c.replace("l", "H"))
c = c.replace("l", "H")
print(c)

# remove space from first and last
c = " Hello world "
print(c)
print(c.strip("o"))

c1 = "oHello worldo"
print(c1.strip("o"))

c = "oHello worldo"
print(c.lstrip("o"))
print(c.rstrip("o"))

# 5
c = "oooooHello  Hello worldo "

#  find("substring to find", from_index)
print(c.find("Hello", 6))  # index of first occurrence
print(c.find("Hello"))
print(c.rfind("Hello"))

#
# c = "Hello world"
# c.startswith()
