import math

"""
Arithmetic operator
+
-
*
/
// - dropped floating point
%
** power

------------------------------------------------
math - abs, power, sqrt

------------------------------------------------
parenthesis
* /
+ -
Left to right

"""

a = 12
b = 13

# اگر به نتیجه جمع در ادامه نیاز دارید نتیجه را در متغیر ذخیره میکنید.
c = a + b
d = a + b - 12

print(c)

print(f"a + b = {a + b}")  # braces
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a ** b = {a ** b}")  # int - 106993205379072
print(f"math.pow(a, b) = {math.pow(a, b)}")  # float - 106993205379072.0
print(f"a % b = {12 % 2}")  # باقی مانده
print(f"math.sqrt(16) = {math.sqrt(16)}")  # رادیکال
print(f"16 ** 0.5 = {16 ** 0.5}")
print(f"16 ** (1 / 2) = {16 ** (1 / 2)}")

print(f"natijeh: {(math.sqrt((12 / 2) ** 2 * 10 - 12) // 4)}")
# d = c + 2
