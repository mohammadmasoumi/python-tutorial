import sys
import functools

sys.setrecursionlimit(10**7) # max depth of recursion

# SOLUTION 1
def cache(f):
    cache.my_cache = {}

    @functools.wraps(f)
    def wrapper(*args):
        key = ", ".join([str(item) for item in args])

        res = cache.my_cache.get(key)
        if not res:
            res = f(*args)
            cache.my_cache[key] = res

        return res

    return wrapper


@cache
def fibo(n):
    if n < 2:
        return 1

    return fibo(n-1) + fibo(n-2)


print(fibo)
print(fibo(100))
print(fibo(1000))
print(fibo(2000))

# SOLUTION 2
"""
See: 
https://stackoverflow.com/questions/815110/is-there-a-decorator-to-simply-cache-function-return-values
https://docs.python.org/dev/library/functools.html#functools.lru_cache
"""
@functools.lru_cache(maxsize=None)
def fibo(n):
    if n < 2:
        return 1

    return fibo(n-1) + fibo(n-2)

print(fibo)
print(fibo(100))
print(fibo(1000))
print(fibo(2000))
print(fibo.cache_info())
