num = int(input("enter a number: "))


"""
Mistake
if num % 3 == 0:
    print("Foo")
if num % 5 == 0:
    print("bar")
if num % 3 == 0 and num % 5 == 0:
    print("FooBar")
"""
# num % 3 == 0 and num % 5 == 0
if num % 15 == 0:
    print("FooBar")  # print(FooBar) WRONG
    # print("FooBar") print('FooBar') CORRECT
# num % 3 and num % 5 == 0 WRONG
# num % 3 == 0 and num % 5 == 0
# logical operator
elif num % 3 == 0 and num % 5 == 0:
    print("FooBar")
elif num % 5 == 0:
    print("bar")
elif num % 3 == 0:
    print("Foo")
