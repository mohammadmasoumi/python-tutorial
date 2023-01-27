# Closure

def installment_rate():
    # bound to function
    # private state
    RATE = 30

    def function2(n):
        return n + n * RATE

    return function2


f = installment_rate()
print(f(100000))
print(f(10000000))

def installment_rate(RATE):
    # bound to function
    # private state
    def function2(n):
        return n + n * RATE

    return function2

installment_rate_20 = installment_rate(20)
installment_rate_30 = installment_rate(30)

print(installment_rate_20(100000))
print(installment_rate_20(1000000000))

print(installment_rate_30(100000))
print(installment_rate_30(1000000000))