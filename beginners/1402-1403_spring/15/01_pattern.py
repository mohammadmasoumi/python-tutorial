n=int(input())


# 
"""

1.
*

2.
  *
 ***
*****

3.

    *
   ***
  *****
 *******
*********
"""
# justification
# rjust(3)
# [ ][ ][*] 
# [ ][*][*]
# [*][*][*]
#  *  *  *  *
# "*" * idx.rjust(n)

# left side
#   *
#  **
# ***
# right side
# *
# **
# ***
#   **
#  ****
# ******
for idx in range(2*n-1):

    left_side = ("*" * (idx+1)).rjust(2*n-1) # statement
    right_side = ("*" * (idx+1)).ljust(2*n-1)[1:]

    print(left_side + right_side)

if n > 1:
    for _ in range(2*n-1):
        print(("*"*(2*n-1)).center(4*n-3))