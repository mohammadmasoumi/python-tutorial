# Immutable
string = "hello world"

# بر اساس فاصله جدا میکند.
# ['Hello', 'world']
print(string.split(' '))

# Hello world
print(string.capitalize())

# Hello World
print(string.title())

# 2
print(string.count('o'))

# 2 - start index
print(string.find('llo'))

# string as a array
# h
print(string[0])
# (space)
print(string[5])

# if string.startswith('ello'):
if string.startswith('hello'):
    print("it starts with hello")

if string.endswith("d"):
    print("it ends with d")

if "hello" in string:
    print(f"Hello is in {string}")

string2 = " hello world "
string3 = "ahello worlda"
# trim
print(string2.strip())
print(string3.strip('a'))

string4 = "Ali"
print(string4.lower())
print(string4.upper())

# string.upper()
# immutable
# string = string.upper()

# the first time l appear
print(string.index('l'))

# اکر همه کاراکترها عدد باشد بولین True را بر میگرداند.
a = "12a*"
print(a.isdigit())

# just alpha + number
a = "12a"
print(a.isalnum())

