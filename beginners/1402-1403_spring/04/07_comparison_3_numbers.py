num1 = int(input())
num2 = int(input())
num3 = int(input())

# num1 = input()
# num2 = input()
# num3 = input()

"""
string comparison
11
2
3
"""

# JAVA and C
# num1 < num2 and num2 < num3

# PYTHON
min_num = None
mid_num = None
max_num = None

if num1 <= num2 <= num3:
    # min_num = num1
    # mid_num = num2
    # max_num = num3
    res = num1, num2, num3
    # print(num1, num2, num3, sep=" <= ")
elif num1 <= num3 <= num2:
    res = num1, num3, num2
    # print(num1, num3, num2, sep=" <= ")
elif num2 <= num1 <= num3:
    res = num2, num1, num3
    # print(num2, num1, num3, sep=" <= ")
elif num2 <= num3 <= num1:
    res = num2, num3, num1
    # print(num2, num3, num1, sep=" <= ")
elif num3 <= num2 <= num1:
    res = num3, num2, num1
    # print(num3, num2, num1, sep=" <= ")
elif num3 <= num1 <= num2:
    res = num3, num1, num2
    # print(num3, num1, num2, sep=" <= ")

print(*res, sep=" <= ")