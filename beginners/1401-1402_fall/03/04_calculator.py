from math import sqrt, ceil, floor

# 12 + 13
"""
12 
+
13
"""

# "12    +    13"
# my_input = input("Enter Equation: ")

# default: " "
# ["12     ", "+", "       13"]
# trim
# my_input = my_input.split()
# operand1 = int(my_input[0].strip())
# operator = my_input[1].strip()
# operand2 = int(my_input[2].strip())

operand1, operator, operand2 = map(
    lambda x: int(x) if x.isdigit() else x , 
    input().split() # "12 + 13" => ["12", "+", "13"]
                                 # [12, "+", 13]
    )
# operand1, operator, operand2 = [12, "+", 13]

print(f"operand1: {operand1}, operator: {operator}, operand2: {operand2}")

# print(ceil(4.6), floor(4.6))
# operand1 = int(input("Enter Operand: "))
# operator = input("Enter Operator: ") 
# if operator != "sqrt":
#     operand2 = int(input("Enter Operand: "))

#                  +
#                 "+"
# print(operand1 operator operand2)

if operator == "+":
    print(operand1 + operand2)
elif operator == "-":
    print(operand1 - operand2)
elif operator == "*":
    print(operand1 * operand2)
elif operator == "**":
    print(operand1 ** operand2)
elif operator == "sqrt":
    res = sqrt(operand1)
    # if res == ceil(res):
    #     print(int(res))
    # else:
    #     print(res)
    print(int(res) if res == ceil(res) else res)
elif operator == "//":
    if operand2 == 0:
        print("Division by zero is not allowed!")
    else:
        print(operand1 // operand2)
elif operator == "/":
    if operand2 == 0:
        print("Division by zero is not allowed!")
    else:
        print(operand1 / operand2)
else:
    print("Invalid operator, Valid operators are: [+, - , /, *]")

