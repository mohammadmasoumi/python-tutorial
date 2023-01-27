# optimized fibo
n = int(input())

# so_far_fibo = {}
# so_far_fibo={}

def fibo(m, so_far_fibo={}):
    # so_far_fibo={}

    if m == 1:
        return 0
    elif m == 2:
        return 1
    else:
        res = so_far_fibo.get(m) 
        if res:
            return res
        else:
            res = fibo(m-2) + fibo(m-1)
            so_far_fibo[m] = res
            return res 

print(fibo(n))