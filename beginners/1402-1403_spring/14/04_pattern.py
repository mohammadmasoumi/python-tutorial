"""
1.
    *

2.
    * 
  * * * (2*n-1)
    * 
3.  
    *  (2*idx-1)
  * * * (2*idx-1)
* * * * * (2*idx-1)
  * * *
    * 
"""
n = int(input()) # n: 3

idx = 1
cnt = 1

# idx = 1, 2, 3, 4, 5, 6
# cnt = 1, 2, 3, 2, 1, 0
while idx <= 2*n-1: # 2*n-1: 5
    # "* ".center(10)
    # "* * * ".center(10)
    # "* * * * * ".center(10)
    # "* * * ".center(10)
    # "* ".center(10)
    print(("* "* (2*cnt-1)).center(2*(2*n-1)))

    if idx >= n:
        cnt -= 1
    else:
        cnt += 1

    idx += 1

cnt = 1
for idx in range(1, 2*n):
    pass
