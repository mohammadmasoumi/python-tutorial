#       012345678910
name = "HEllo World"
# [NOTE]: in name variable, space(name[5]) is a character
# name2 = "HelloWorld"


# print(name[0])
# print(name[5])
# print(len(name))
# ----------------------
# ASCII code
# print(ord('a'))
# print(ord('z'))
#
# print(ord('A'))
# print(ord('Z'))
# ----------------------
# name = "Hello World"

# print(chr(ord(name[0]) + 32))
# print(ord('h'))
# print(name)
print(name)
char = chr(ord(name[0]) + 32)
name = char + name[1:]

ascii_code = ord(name[1])
#  ord('A')         ord('Z')
if 65 <= ascii_code <= 90:
    ascii_code += 32
    # ascii_code = ascii_code +  32

char = chr(ascii_code)
name = name[0] + char + name[2:]

print(name)
# h + e + llo World


# print(chr(ascii_code))

# name1 = chr(ord(name[1]))
#
# print(name0 + name1)

# list1 = [1, 2 , 4]
# list1.append(4)


# --------------
# print(chr(104))
