"""
1. --------------
a

2. --------------
  a
a-b-a
  a

3. --------------
    a
  a-b-a
a-b-c-b-a
  a-b-a
    a

4. --------------
      a
    a-b-a
  a-b-c-b-a
a-b-c-d-c-b-a
  a-b-c-b-a
    a-b-a
      a
"""
import string
characters = string.ascii_lowercase

n = int(input())

for index in range(n):
    left_side = "-".join(characters[:index+1])
    right_side = left_side[-2:: -1]

    print((left_side + right_side).center(4 * n - 1))

for index in range(n-2, -1, -1):
    left_side = "-".join(characters[:index+1])
    right_side = left_side[-2:: -1]

    print((left_side + right_side).center(4 * n - 1))
