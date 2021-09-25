# False values => False, 0, None
# True values => True, 1, 2, 3, ...

a = 0
b = 1

# do not check b / a because a is false
if a and b / a:
    print(b / a)

# do not check a because b is true
# ZeroDivisionError: division by zero
if b or a:
    # print(f"b/a: {b / a}")
    pass

c = 10
d = 5
if c:
    print(c)

if c / d:
    print(c / d)

if 0.1:
    print(0.1)

if (10 * 2 - 20) == 0:
    print("Hello")

if c == 10:
    print("Hello")

if c == 10:
    pass
elif c == 20:  # else if
    pass
else:
    pass

e = 100

# true value if condition else false value
# ternary operator
# c = condition ? true_value : false_value
inline_if = "True" if e == 100 else "False"
# inline_if = "True" if e == 100 (WRONG)


