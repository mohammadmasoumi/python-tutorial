# 5 => Foo
# 3 => Bar
# 3 and 5 => FooBar

a = int(input())

# if True:
#     pass
# else:
#     if False:

if a % 3 == 0 and a % 5 == 0:
    print("FooBar")
elif a % 5 == 0:
    print("Foo")
elif a % 3 == 0: # a % 15 == 0
    print("Bar")
else:
    print("Not divided by 3 or 5")


# if a % 3 == 0 and a % 5 == 0:
#     print("FooBar")
# if a % 5 == 0:
#     print("Foo")
# if a % 3 == 0: # a % 15 == 0
#     print("Bar")
# else:
#     print("Not divided by 3 or 5")