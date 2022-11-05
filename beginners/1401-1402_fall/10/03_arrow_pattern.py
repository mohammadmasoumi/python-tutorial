"""
1.
*

3. 
  *
 ***
*****
 ***
 ***
 ***

5.
    *
   ***
  *****
 ********
**********
  *****
  *****
  *****
  *****
  *****
"""

n = int(input())
length = 2 * n - 1

for row in range(n):
    print(("*" * (2 * row + 1)).center(length))

for row in range(n):
    print(("*" * (n)).center(length))
