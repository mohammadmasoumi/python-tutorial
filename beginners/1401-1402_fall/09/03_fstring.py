import math
math.sqrt()
math.ceil()
# -------------------
from math import sqrt, ceil 

from my_math import hello

hello()
my_list = [1, 2, 3 , 4]

# [1, 2, 3 , 4]
print(f"[{', '.join(map(lambda x: str(x),my_list))+ ']': <20}")

# 4 5 6
# ["4", "5", "6"]
a = "4*5*6".split("*")
print("4*5*6".split("*"))
print(a)

print((my_list.append(10)))
print((my_list.append(10), ))
print(my_list)