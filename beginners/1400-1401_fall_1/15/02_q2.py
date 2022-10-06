# import string
#
# print(string.ascii_lowercase)

#        01234567
alpha = "abcdefghijklmnopqrstuvwxyz"

n = int(input())
# for idx in range(n, 1, -1):
for idx in range(n - 1):
    # 0 -> e
    # 1 -> de
    # 2 -> cde
    # 4
    # print(f"idx: {idx}, alpha[{n - idx - 1}: {n}], value: {alpha[n - idx - 1: n]}")
    right = "-".join(alpha[n - idx - 1: n])
    left = right[::-1]

    # print(f"n: {n}, idx: {idx} value: {n - (2 * idx)}")
    spaces = "".join([" "] * (((n - 1 - (idx + 1)) * 2)))  # index: 3 n: 6

    print(spaces + left + right[1:])
    # print("-".join(alpha[n - idx - 1: n]))
