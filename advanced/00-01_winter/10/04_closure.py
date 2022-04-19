

def make_multiplier_of(x):
    # x binds to the function

    def multiplier(n):
        return n * x

    return multiplier


multiplier_by_3 = make_multiplier_of(3)
print(multiplier_by_3(10))
print(multiplier_by_3(11))
print(multiplier_by_3(12))
print(multiplier_by_3(13))

multiplier_by_4 = make_multiplier_of(4)
print(multiplier_by_4(10))

