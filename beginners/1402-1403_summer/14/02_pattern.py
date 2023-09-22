"""

1. 
  *

2. 
  *  
 ***
  *
3.
|  *  | "  *  " 0 
| *** | " *** " 1
|*****| "*****" 2
_______
| *** |         1 (n-2)
|  *  |         0
                -1
n: 3

starts: 1 | index: 0 | space: 2
starts: 3 | index: 1 | space: 1
starts: 5 | index: 2 | space: 0
row: 2*index+1
space: n-1-index

height: 2*n-1
max_width: 2*n-1
"""

n = int(input())

# for i in range(n):
#     count = 2*i +1
#     starts = "*" * count
#     # spaces = " " * (n - 1 - i)
#     # print(spaces + starts)

#     print(starts.center(2*n - 1))

# for i in range(n-2, -1, -1):
#     count = 2*i +1
#     starts = "*" * count
#     # spaces = " " * (n - 1 - i)
#     # print(spaces + starts)

#     print(starts.center(2*n - 1))

"""
|  *  | stage: 0, index: 0  
| *** | stage: 1, index: 1
|*****| stage: 2, index: 2  ------ n=3
| *** | stage: 3, index: 1
|  *  | stage: 4, index: 0        

if stage < n
    index++
else:
    index--
"""
# n: 3, stage: 0, index: 0
stage = 0
index = 0
while stage < 2*n-1: # 2*n-1: 5
    # n: 3, stage: 0, index: 0
    # n: 3, stage: 1, index: 1
    # n: 3, stage: 2, index: 2

    # count: 1
    # count: 3
    # count: 5
    count = 2*index +1 
    # "*"
    # "***"
    # "*****"
    starts = "*" * count
    # "  *  "
    # " *** "
    # "*****"
    print(starts.center(2*n - 1))

    # n: 3, stage: 1, index: 1
    # n: 3, stage: 2, index: 2
    # n: 3, stage: 2, index: 2
    if stage < n - 1:
        index += 1
    else:
        index -= 1
    
    stage += 1
    


# patterns = [
#     "*",
#     """
#       *
#      ***
#       *
#     """,
#     """
#       *
#      ***
#     *****
#      ***
#       *
#     """
# ]
