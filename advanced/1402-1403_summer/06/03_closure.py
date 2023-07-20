def multiplier(n):
    # local state 
    multiplier.count = 0

    def mul(m):
        # m: 10
        multiplier.count += 1
        return m * n

    return mul


multiply_by_3 = multiplier(3)
print(multiply_by_3(10))
print(multiply_by_3(11))
print(multiplier.count)

multiply_by_4 = multiplier(4)
print(multiply_by_4(11))
print(multiplier.count)
