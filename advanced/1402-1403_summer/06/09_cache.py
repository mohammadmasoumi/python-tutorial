# cache
mem_cache = {}

def cache(f):  # call once
    """
    {
        args      res
        (10, 12): 22,
        (10, 13): 23
    }
    
    """
    def wrapper(*args):  # call many times
        # hit
        cached_res = mem_cache.get(args)
        if cached_res:
            print("returned value from cache!")
            return cached_res

        # miss
        res = f(*args)
        mem_cache[args] = res
        return res

    return wrapper

# wrapper = cache(add)


@cache
def add(a, b):
    return a + b


# wrapper = cache(mul)
# mul() === wrapper()
@cache
def mul(a, b):
    return a * b


print(add(10, 12))
print(mul(10, 12))
