


# start:end:step

# create a sequence of numbers
# seq = range(0, 100, 2)
# print(seq) # range(0, 100, 2)
# print(list(seq))

# for item in range(0, 100, 2):
#     print(item)

# print("*".center(5))
# print("***".center(5))
# print("*****".center(5))
# print("***".center(5))
# print("*".center(5))

# 
n = int(input())

# range(3)
# print(list(range(3)))
max_width = 2 * n - 1

for idx in range(n):
    # idx: 0 => *
    # idx: 1 => ***
    # idx: 2 => *****
    # (2 * idx) + 1
    # " " * (2 * idx + 1)
    pattern = "*" * (2 * idx + 1)
    print(pattern.center(max_width))

# idx: 0 => ***** 5
    # idx: 1 => *** 3
    # idx: 2 => * 1
    # y2 - y1
    # x2 - x1
    # 3 - 5
    # 1 - 0
    # a: -2
    # y = ax + b
    # 5 = -2 * 0 + b => 5
    # y = -2 * b + 5

for idx in range(n - 2,-1, -1):
    pattern = "*" * (2 * idx + 1)
    # pattern = "*" * ((-2 * idx) + max_width)
    print(pattern.center(max_width))


# for idx in range(1, n):
#     pattern = "*" * ((-2 * idx) + max_width)
#     print(pattern.center(max_width))


for idx in range(n):
    pattern = "*" * 3
    print(pattern.center(max_width))


