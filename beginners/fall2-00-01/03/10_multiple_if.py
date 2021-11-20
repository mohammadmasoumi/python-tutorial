"""
A -> 20
B -> 19
C -> 18
D -> 17
else -> 10
"""

mark = input()

# without elif
# if mark == 'A':
#     print(20)
# else:
#     if mark == 'B':
#         print(19)
#     else:
#         if mark == 'C':
#             print(18)
#         else:
#             if mark == 'D':
#                 print(17)
#             else:
#                 print(10)

# with elif
if mark == "A" or mark == "Z":
    print(20)
elif mark == "B":
    print(19)
elif mark == "C":
    print(18)
elif mark == "D":
    print(17)
else:
    print(10)
