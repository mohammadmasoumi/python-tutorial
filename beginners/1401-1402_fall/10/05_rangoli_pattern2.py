"""
1. --------------
a

2. --------------
  b
b-a-b
  b

3. --------------
    c
  c-b-c
c-b-a-b-c
  c-b-c
    c

4. --------------
      d
    d-c-d
  d-c-b-c-d
d-c-b-a-b-c-d
  d-c-b-c-d
    d-c-d
      d
"""
import string
characters = string.ascii_lowercase

n = int(input())
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
