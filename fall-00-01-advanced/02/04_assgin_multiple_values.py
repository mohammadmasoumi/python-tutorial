# x = 12
# y = 13
# z = 14
x, y, z = 12, 13, 14
#  cannot unpack non-iterable int object
x1, y1 = 12, 12

# assign multiple variables with the same value
x2 = y2 = 12

# unpacking
# iterable - iter - you can loop over it.
# orange = fruit[0]
# apple = fruit[1]
fruit = ["Orange", "Apple"]
orange, apple = fruit
# ValueError: not enough values to unpack (expected 3, got 2)
# orange, apple, banana = fruit
