# print(string.ascii_lowercase)
n = int(input())

#             012
characters = "abcdefghijklmnopqrstuvwxyz"

width = 4 * n - 3

def print_row(idx):
    sub_string = characters[n - (idx + 1): n]
    right_side = "-".join(sub_string)
    left_side = right_side[-1:0:-1]

    print((left_side + right_side).center(width))


for i in range(n):
    print_row(i)


for i in range(n - 2, -1, -1):
    print_row(i)


# OR 
# for i in range(n-2):
#     sub_string = characters[i + 1: n]
#     right_side = "-".join(sub_string)
#     left_side = right_side[-1:0:-1]

#     print((left_side + right_side).center(width))
