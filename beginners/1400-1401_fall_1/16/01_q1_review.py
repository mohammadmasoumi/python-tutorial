s = "abcdefghijklmnopqrstuvwxyz"

n = int(input())

sub_s = s[:n]
reverse_sub_s = sub_s[::-1]

# print(f"sub_s: {sub_s}")
# print(f"reverse_sub_s: {reverse_sub_s}")

# for idx in range(n - 1):
for idx in range(n):
    # idx 0: d [0:1] [0:idx+1]
    # idx 1: dc [0:2] [0:idx+1]
    # idx 2: dcb [0:3] [0:idx+1]
    left = "-".join(reverse_sub_s[:idx + 1])
    right = left[::-1]
    row = (left + right[1:]).center(2 * 2 * (n - 1) + 1)
    # print(row.replace(" ", "-"))
    print(row)

for idx in range(1, n):
    # n: 4, idx: 0
    # reverse_sub_s[0:3] dcb d-c-b-c-d
    # reverse_sub_s[0:2] dc d-c-d
    # reverse_sub_s[0:1] d d
    # reverse_sub_s = dcba

    left = "-".join(reverse_sub_s[:n - idx])
    right = left[::-1]
    row = (left + right[1:]).center(2 * 2 * (n - 1) + 1)
    # print(row.replace(" ", "-"))
    print(row)