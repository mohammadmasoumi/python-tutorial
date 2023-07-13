
a = 12
b = 13
# Return whether an object is an instance of a class or of a subclass thereof.
print(type(a))
if isinstance(a, int) and isinstance(b, int):
    print("a is an int")
    c = a + b

if isinstance(a, (int, str, float)):
    print("a is an int, str, float")
    c = a + b

my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(type(item))
    if isinstance(item, int):
        print("I am doing sth on the item")


def add(a, b):  # a, b: params
    # a: 10, b: 12
    # a: 11, b: 12
    return a + b


add(10, 12)  # 10, 12 argument
add(11, 12)  # 11, 12 argument
