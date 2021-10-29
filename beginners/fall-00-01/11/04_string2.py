s = "Hello world"
# s = "Hello*world" => False
# s = "Hello-world" => False
# s = "Hello world1" => False because of space

# Return True if the string is an alpha-numeric string, False otherwise.
# False => space
print(s.isalnum())

#
s1 = "12920a"
s2 = "12920"
s3 = "a"
print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())

#
print("==========================================")
"""
A string is a digit string if all characters in the string are digits and there
is at least one character in the string.
"""
s4 = ""
print(s1.isdigit())
print(s4.isdigit())
print(s2.isdigit())
print(s.isdigit())  # False

#
print("==========================================")
a = oct(80)
s5 = f"{a}"
print(f"oct(a): {a}")
print(s5.isdecimal())

# isinstance
print("==========================================")
print(f"isinstance(s5, int): {isinstance(s5, int)} | {type(s5)}")
print(f"isinstance(s5, float): {isinstance(s5, float)} | {type(s5)}")
print(f"isinstance(s5, str): {isinstance(s5, str)} | {type(s5)}")
print(f"isinstance(s5, bool): {isinstance(s5, bool)} | {type(s5)}")
print(f"isinstance(s5, list): {isinstance(s5, list)} | {type(s5)}")

if isinstance(s5, str):
    print(f"{s5} is a string")
else:
    print(f"{s5} is not a string")

print(s.zfill(20))
print(s[-5:].zfill(20))  # 00000000000000 world
print(s[-1:].zfill(20))  # 0000000000000000000d
