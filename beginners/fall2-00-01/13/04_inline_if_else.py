
condition = True

#
a_true = "true"
a_false = "false"

number = a_true if condition else a_false
number = "Hello" if condition else "Bye"
number = "Hello" if condition else None


if condition:
    number = a_true
else:
    # number = a_false
    print("Invalid number")


