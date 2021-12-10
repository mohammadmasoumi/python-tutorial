"""
5
1 + 2 + 3 + 4 + 5
"""

counter = 0

# def acc(num):
#     global counter
#
#     counter += 1
#     print(f"num: {num}, counter: {counter}")
#     return acc(num)

"""


"""


# acc(4)
def acc(num):
    print(f"num: {num}")

    if num == 1:
        return num

    # acc (4) = 24
    # acc (3) = 6
    # acc (2) = 2
    # acc (1) = 1
    a = acc(num - 1)
    print(f"a: {a}")

    return num * a


print(acc(4))
