import math

operand1 = int(input())
opt = input()

if opt == 'sqrt':
    if operand1 > 0:
        print(math.sqrt(operand1))
    else:
        print("Can't sqrt of negative numbers!")
elif opt == 'abs':
    print(abs(operand1))
else:
    operand2 = int(input())

    if opt == '+':
        print(operand1 + operand2)
    elif opt == '-':
        print(operand1 - operand2) 
    elif opt == '*':
        print(operand1 * operand2) 
    elif opt == '/': # corner case
        if operand2 == 0:
            print("ZeroDivisionException: you can't divide a number by zero!")
        else:
            print(operand1 / operand2) 
    elif opt == '//':
        if operand2 == 0:
            print("ZeroDivisionException: you can't divide a number by zero!")
        else:
            print(operand1 // operand2) 

