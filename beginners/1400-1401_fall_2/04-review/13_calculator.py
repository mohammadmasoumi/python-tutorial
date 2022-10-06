"""
operand 12
operator + / * -
operand 13

#
12
+
13

=> 12 + 13
"""
operand1 = int(input())
operator = input()  # str "+", "/", "-". "*"
operand2 = int(input())

# operand1 operator operand1
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
#           int   + str +    int
# print(f'{operand1 + operator + operand2}')
# print(f'{operand1 + "+" + operand2}')

# "+", +

# operator "+"
# operand1 + operand2

# a = 12
# if a == 12:
#     print(a)

# b = "+"
# if b == "+":
#     print(b)


# Corner case
# ZeroDivisionError: division by zero

if operator == "+":
    print(operand1 + operand2)

elif operator == "-":
    print(operand1 - operand2)

elif operator == "*":
    print(operand1 * operand2)

# elif operator == "/" and operand2 == 0:
#     print("ZeroDivisionError")

elif operator == "/":
    if operand2 != 0:
        print(operand1 / operand2)
    else:
        print("ZeroDivisionError")
else:
    print("Invalid!")
