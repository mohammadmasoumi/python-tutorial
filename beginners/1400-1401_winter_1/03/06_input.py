# built-in function
# type, print, int, str, float. bool
# input 

# a, b str
a = int(input("Input a: ")) # "12"
b = int(input("Input b: ")) # "13"

# a = int(a) # 12 = int("12")
# b = int(b) # 13 = int("13")
print(type(a))
print(type(b))

c = a + b
print("result:", c) # 12 + 13
print("result type:", type(c))
# print(int(a) + int(b))