# def fibo(n):
#     if n < 3:
#         return n

#     return fibo(n-1) + fibo(n-2)


# print(fibo(5))

"""

1

 1
212
 1

  1
 212
32123
 212 
  1

   1
  212 
 32123
4321234
 32123
  212 
   1
"""

n = int(input())
idx = 0
cnt = 0

# n: 3
# idx: 0, cnt: 0
# idx: 1, cnt: 1
# idx: 2, cnt: 2
# idx: 3, cnt: 1
# idx: 4, cnt: 0
while idx < 2*n-1:
    # cnt+1 -> 0
    left_side = " ".join(map(str, range(cnt+1, 0, -1)))
    right_side = " ".join(map(str, range(2, cnt+2)))

    additional = 0
    if n >= 10:
        # 10 -> 2
        # 11 -> 4
        # (n - 9) doraghami
        additional = (n - 9) * 2

    print((left_side + " " + right_side).center((4*n-3)+additional))

    if idx >= n-1:  # n-1: 2
        cnt -= 1
    else:
        cnt += 1

    idx += 1
