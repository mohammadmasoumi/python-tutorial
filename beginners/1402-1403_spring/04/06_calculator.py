num1 = int(input())
operator = input()
num2 = int(input())

res = None

if operator == "+":
    # print(num1 + num2)
    res = num1 + num2
elif operator == "-":
    # print(num1 - num2)
    res = num1 - num2
elif operator == "*":
    # print(num1 * num2)
    res = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("can't divide by zero.")
    else:
        # print(num1 / num2)
        res = num1 / num2

if res != None:
    print(f"res: {res}")