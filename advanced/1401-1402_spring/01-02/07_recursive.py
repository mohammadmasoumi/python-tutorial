

def factoril(n):
    # n: 5
    # n: 4
    # n: 3
    # n: 2
    # n: 1
    if n == 1:
        return 1
    else:
        # factoril(1) = 1
        # factoril(2): 2 * 1
        # factoril(3): 3 * 2
        # factoril(4): 4 * 6
        # factoril(5): 5 * 24

        # factoril(1) = 1
        # factoril(2): 2 * factoril(1)
        # factoril(3): 3 * factoril(2)
        # factoril(4): 4 * factoril(3)
        # factoril(5): 5 * factoril(4)
        return n * factoril(n-1)




"""
|             |
|             |
|             |
|             |
|             |
|             |
|             |
______________
     stack

|             |
|             |
|             |
|             |
|             |
|             |
| factoril(5) |
______________
     stack

|             |
|             |
|             |
|             |
|             |
| factoril(4) |
| factoril(5) |
______________
     stack

|             |
|             |
|             |
|             |
| factoril(3) |
| factoril(4) |
| factoril(5) |
______________
     stack

|             |
|             |
|             |
| factoril(2) |
| factoril(3) |
| factoril(4) |
| factoril(5) |
______________
     stack

|             |
|             |
| factoril(1) |
| factoril(2) |
| factoril(3) |
| factoril(4) |
| factoril(5) |
______________
     stack
"""

# print(120)
print(factoril(5))