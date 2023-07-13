"""
built-in function

input() -> get sth from terminal 
print() -> print sth in terminal 
"""

a = input()

# type conversion
# cast
print(a, type(a))  # a: "12", a: "ali"

b = 12
#           ضمنی
#           implicit
print(b)  # 12 -> "12"

# -------
#             Hint
name = input("enter your name:")
email = input("enter your email: ")
password = input("enter your password: ")
print(name, email, password)
