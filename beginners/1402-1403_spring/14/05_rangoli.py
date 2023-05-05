"""
1.
a

2.

  a
a-b-a
  a

3.
    a
  a-b-a
a-b-c-b-a
  a-b-a
    a

4.
        a
      a-b-a
    a-b-c-b-a
  a-b-c-d-c-b-a
    a-b-c-b-a
      a-b-a
        a    

        a-b-a
        a-b-c-b-a
        "hello"[::-1]
"""
import string

n = int(input())
# alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = string.ascii_lowercase

# print(alphabet[:2]) # "ab"
# print("-".join(alphabet[:n])) 


idx = 1
cnt = 1

while idx <= 2*n-1:
    slice = alphabet[:cnt]
    left_side = "-".join(slice)
    # a-b left_side
    # b-a left_side[::-1]
    # -a left_side[::-1][1:]
    # a-b-a
    # a-b-c-d-ee-d-c-b-a
    # a-b-c-d-e-d-c-b-a
    right_side = left_side[::-1][1:]

    print((left_side + right_side).center(4*n-3))

    """
    1 => 1
    2 => 5
    3 => 9

        9-5
    a = --- = 4
        3-2

        y2-y1
    a = -----
        x2-x1

    y=ax+b
    y = 4x+b

    9 =  4*(3) + b
    b => -3

    y=4x-3
    """

    if idx >= n:
        cnt -= 1
    else:
        cnt += 1

    idx += 1