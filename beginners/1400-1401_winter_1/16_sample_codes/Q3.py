"""
1
121
12321
1234321
123454321
"""

pattern_num = int(input())

for row in range(1, pattern_num + 1):

    left_side = ""
    for num in range(1, row + 1):
        left_side += str(num)

    right_side = left_side[-2:: -1]
    pattern = left_side + right_side
    print(pattern)
