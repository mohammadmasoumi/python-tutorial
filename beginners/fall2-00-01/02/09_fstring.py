# fstring
# formatted string

# After python 3.6
a = "Mohammad"

print(f"Calculating invoice has been started for {12} users.")
print("Calculating invoice has been started for " + "12" + " users.")
print("Hello " + a)
print("Hello {a}")
print(f"Hello {12 - 2 * 10}")
print(f"Hello {a}")
print(f"Hello {a}{a} {a}")

# SyntaxError: f-string: empty expression not allowed
# print(f"Hello {a} {}{a}{a}{a}")

# format

print("Hello {}".format(a))
# print("Hello {} {}".format(a))
print("Hello {} {}".format(a, a))
print("Hello {}".format("Mohammad", "Ali"))

# ZeroDivisionError: division by zero
# print("Hello {}".format("Mohammad", 12/0))
print("Hello {a1} {b2}".format(b2="Ali", a1="Mohammad"))
