# is instance
a = 12

if type(a) == int:
    print("Hello")

if isinstance(a, int) or isinstance(a, str):
    print("Hello")

if isinstance(a, (int, str)):
    print("Hello")