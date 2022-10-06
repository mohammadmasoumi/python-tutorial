# fstring => formatted string

# sep?
print("result:", 20) # result:20 . result: 20

a = 20
print(f"result: {a}")
# print(f"result: {b}") # NameError: name 'b' is not defined
print(f"result:{a}")
print("result:", a)
#  if a == 12:
#      print("Hello")
name = "asghar"
father_name = "akbar"
print(f"Hello, {name}, How are you? How is {father_name}? ...")
print("Hello, asghar, How are you? How is akbar? ...")
print("Hello, {name}, How are you? How is {father_name}? ...")
print("Hello,", name, ", How are you? How is", father_name, "? ...")
