n = int(input())

"""
n: 198 => 18
n: 18 => 9
m: 9 
"""

# n > 9
# while True:

#     if n < 10:
#         break

#     num = n
#     s = 0
#     # num: 198, s: 0
#     while num > 0:
#         # yekan: 8, num: 198, s: 0
#         # yekan: 9, num: 19, s: 8
#         # yekan: 1, num: 1, s: 17
#         yekan = num % 10
#         # yekan: 8, num: 198, s: 8
#         # yekan: 9, num: 19, s: 17
#         # yekan: 1, num: 1, s: 18
#         s += yekan
#         # yekan: 8, num: 19, s: 8
#         # yekan: 9, num: 1, s: 17
#         # yekan: 1, num: 0, s: 18
#         num = num // 10

#     n = s
#     # s: 18, n: 18

# print(n)

"""
39 => 12 => 3
38 => 11 => 2
37 => 10 => 1
36 => 9
35 => 8
34 => 7
33 => 6
32 => 5
31 => 4
30 => 3
29 => 11 => 2
28 => 10 => 1
27 => 9
26 => 8
"""
n %= 9
# print(9 if n == 0 else n)
# bool(n) 
print(9 if not n else n)
