# Closuer

def multiplier(n):
    # n: 3
    # binding n to mul
    def mul(m):
        # m: 10
        return m * n
    return mul

"""
def mul(m):
    return m * n

def multiplier_by_3(m):
    # n: 3
    return m * n
"""
multiplier_by_3 = multiplier(3)
print(multiplier_by_3(10))
print(multiplier_by_3(9))

multiplier_by_4 = multiplier(4)
print(multiplier_by_4(10))
print(multiplier_by_4(9))