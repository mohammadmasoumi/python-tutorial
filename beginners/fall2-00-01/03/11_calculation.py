"""
operand1 12
operator + * / ** // -
operand2 2

sample input:
# 1
12
+
2
14

# 2
13
**
2
169
"""
num1 = int(input())
opt = input()
num2 = int(input())

if opt == "*":
    print(num1 + num2)
elif opt == "-":
    print(num1 - num2)
elif opt == "/":
    if num2 == 0:
        print("Wrong!")
    else:
        print(num1 / num2)
elif opt == "+":
    print(num1 + num2)
elif opt == "**":
    print(num1 ** num2)
elif opt == "//":
    print(num1 // num2)
