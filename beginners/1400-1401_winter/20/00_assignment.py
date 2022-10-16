# پشته
stack = []
status = None
# ())
# ))))
# ))((
for character in input():
    if character == "(":
        stack.append(character)
    elif character == ")":
        if len(stack) == 0:
            print("Invalid")
            # status = "Invalid"
            break
        else:
            stack.pop()
else:
    if len(stack) == 0:
        print("Valid")
    else:
        print("Invalid")

# status = 0, [], "", None, False
# not status => True 
# if len(stack) == 0 and not status:
#     status = "Valid"
# else:
#     status = "Invalid"

# print(status)