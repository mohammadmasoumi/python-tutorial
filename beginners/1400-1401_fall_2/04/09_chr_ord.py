item1 = "A"
item2 = "B"
item3 = "C"

# item1 = 'a'
#         65   + 32
# chr(97)
c = ord(item1) + 32
item1 = chr(c)
print(chr(c))
print(item1)
# print(chr(ord(item1) + 32))
# print(ord('a'))

print("-----------------------")
#       012
name = "ALI"
# print(name.lower())
# ali
c1 = chr(ord(name[0]) + 32)
c2 = chr(ord(name[1]) + 32)
c3 = chr(ord(name[2]) + 32)

print(c1 + c2 + c3)
