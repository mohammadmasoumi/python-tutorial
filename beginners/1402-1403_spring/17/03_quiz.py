string = input()

stack = [] 
# push 
# pop

# Stack
# First In Last out 
# FILO

# Queue 
# FIFO

is_valid = True 

for char in string:
    if char == "(":
        stack.append(char)
    elif char == ")":
        if len(stack) > 0:
            stack.pop() # ())
        else:
            is_valid = False
            break

# (()
if len(stack) > 0:
    is_valid = False

if is_valid:
    print("Valid")
else:
    print("Invalid")