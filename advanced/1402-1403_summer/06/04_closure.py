# closure

def multiplier(n):
    # local state
    count = 0

    def mul(m):
        nonlocal count
        count += 1
        mul.count = count
        return m * n

    return mul


multiply_by_3 = multiplier(3)
print(multiply_by_3(10))
print(multiply_by_3(11))
print(multiply_by_3.count)

multiply_by_4 = multiplier(4)
print(multiply_by_4(11))
print(multiply_by_4.count)

multiply_by_5 = multiplier(5)
print(multiply_by_5(11))
print(multiply_by_5.count)

print(multiply_by_4(11))
print(multiply_by_4.count)
