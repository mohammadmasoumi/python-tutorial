"""
input:
12 + 13
output:
12 + 13 = 25
"""

import sys

args = input().split()

first, operator, second = int(args[0]), args[1], int(args[2])

# result
res = 0
has_exception = False

if operator == '+':
    res = first + second
elif operator == '-':
    res = first - second
elif operator == '/':
    if second == 0:
        has_exception = True
        sys.stderr.write("Division by zero. second number must not be zero!")
    else:
        res = first / second
elif operator == '*':
    res = first * second
else:
    sys.stderr.write(f"Invalid operator: {operator}")

if not has_exception:
    sys.stdout.write(f"{first} {operator} {second} = {res}")
