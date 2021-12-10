# یک شرط پایان recursion
# call function recursively

def fibo(n, node="init"):
    print(f"n: {n}, node: {node}")

    if n == 1 or n == 2:
        return 1

    return fibo(n - 1, "right") + fibo(n - 2, "left")


print(fibo(5))
# print(fibo(7))
# print(fibo(8))
# print(fibo(9))
# 0, 1, 1, 2, 3, 5, 8, 11, 19, ...
