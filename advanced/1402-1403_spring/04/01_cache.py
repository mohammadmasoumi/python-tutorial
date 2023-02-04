import functools

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
# print(fibo(100))
