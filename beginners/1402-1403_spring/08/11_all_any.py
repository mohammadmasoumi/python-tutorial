# truthy falsy

# 0 "" [] 0.0 False

# all: at least one element falsy => False
print(all([20, 20, 20, 1])) # True
print(all([20, 20, 20, 0])) # False
print(all([20, 20, 20, ""])) # False
print(all([20, 20, [], ""])) # False

# any: at least one element truthy => True
print(any([20, 20, 20, 1])) # True
print(any([1, 0, 0.0, "",[]])) # True
print(any([False, 0, 0.0, "",[]])) # False


# builtin function
# min, max, sum, all, any
# int, str, print, bool, list, float, input


