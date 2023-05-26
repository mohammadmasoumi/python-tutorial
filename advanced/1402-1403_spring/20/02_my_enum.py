from my_ennum import MyEnum


class Color(MyEnum):
    RED = 1  # Member (name, value)
    GREEN = 2
    BLUE = 3

    # prop = 4
    # ASGHAR = 4


print(Color.RED.value)

print("----------")
# iter(Color)
for color in Color:
    print(color.name, color.value)
print("----------")


# class A:
#     def __iter__(self):
#         pass

# a = A()

# for item in a:
#     pass