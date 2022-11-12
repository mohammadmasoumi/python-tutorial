# 189 = 18 = 9

# n = int(input())

# # n : 189
# # n: 18
# # n: 9

# # 1.
# while True:

#     if n < 10:
#         break

#     # num: 198
#     # yekan: 8
#     # num: 19
#     # yekan: 9
#     # num: 1
#     # yekan: 1
#     # num: 0
#     # new_n = 0
#     # num = n
#     # while num > 0:
#     #     yekan = num % 10
#     #     num = num // 10
#     #     new_n += yekan
#     # n = new_n

#     new_n = 0
#     # "198"
#     # digit: "1"
#     # digit: "9"
#     # digit : "8"
#     for digit in str(n):
#         new_n += int(digit)

#     n = new_n

# print(n)

# 2.

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
"""
n = int(input())
n %= 9
print(9 if n == 0 else n)
