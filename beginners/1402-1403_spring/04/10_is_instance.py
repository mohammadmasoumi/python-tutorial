a = 12

print(type(a))

# It's not professional
if type(a) == int:
    print("I found an INT")

if isinstance(a, int):
    print("I found an INT")

if isinstance(a, int) or isinstance(a, str):
    print("I found an INT OR STRING")

if isinstance(a, (int, str)):
    print("I found an INT OR STRING")