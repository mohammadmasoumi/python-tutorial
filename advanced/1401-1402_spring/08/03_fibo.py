

def fibo(num, b):

    if num <= 2:
        return 1

    print(f"fibo({num}, {b}) = fibo({num - 1}) and fibo({num-2})")

    return  fibo(num - 1, "left") + fibo(num - 2, "right")


print(fibo(6, ""))