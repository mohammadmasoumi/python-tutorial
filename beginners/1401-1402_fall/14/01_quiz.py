"""
(()())
"""
n = input()

# try:
#     eval(n)
# except SyntaxError:
#     print("Invalid")
# else:
#     print("Valid")

stack = []

# (()
# ))))))
# ())()()()()(
# X^100+X*2

#   *
# ())()()()()(
# stack: []

for item in n:
    if item == "(":
        stack.append(item)
    elif item == ")":
        if len(stack) > 0:
            stack.pop()
        else:
            print("Invalid")
            break
else:
    if len(stack) == 0:
        print("Valid")
    else:
        print("Invalid")

