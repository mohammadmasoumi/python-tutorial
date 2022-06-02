import time

memory = {}
# print(f"fibo({num}) = fibo({num - 1}) and fibo({num-2})")

# def timer(func):
#     def wrapper(*args, **kwargs):
#         s1 = time.perf_counter()
#         res = func(*args, **kwargs)
#         s2 = time.perf_counter()

#         print(f"[{func.__name__}]: {s2-s1}")

#         return res

#     return wrapper


# @timer
def fibo1(num):
    if num <= 2:
        return 1
    
    if memory.get(num):
        return memory.get(num)
    else:
        res = fibo1(num - 1) + fibo1(num - 2)
        memory[num] = res
    return res

# @timer
def fibo2(num):
    if num <= 2:
        return 1
    
    return fibo2(num - 1) + fibo2(num - 2)


s1 = time.perf_counter()
print(fibo1(40))
s2 = time.perf_counter()
print(fibo2(40))
s3 = time.perf_counter()


print(s2-s1)
print(s3-s2)