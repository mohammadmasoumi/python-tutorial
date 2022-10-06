# string

a = "Hello"
print(a.upper())  # HELLO
print(a.lower())  # hello

# ----------------------
b1 = "ali@gmail.com"
b2 = "Ali@gmail.com"

print(b1 == b2)
print(b1 == b2.lower())
print(b1.title())  # upper the first character

#
c = "the squad game"
print(c.title())

# join
print("-".join(["1", "2", "3"]))
print("-".join("asghar"))

print(["1", "2", "3"])
print("[", ", ".join(["1", "2", "3"]), "]")

# split
print(["1", "2", "3"])
print(", ".join(["1", "2", "3"]))
print(", ".join(["1", "2", "3"]).split(", "))


