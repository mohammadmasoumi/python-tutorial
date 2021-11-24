a = 12.09387376
a1 = 12.032987697856435638456384765384
a2 = 2309127423647238647263846238476238742

# float
print(f"number: {a: .2f}")  # float
print(f"number: {a:.0f}")  # float
print(f"{a1}")
print(a1)  # 15
# print(f"number: {a:.2f}")  # float


# str
b = "abc"
print(f"{b: >10}")
print(f"{b: <10}")

# int
c = 2
print(f"{c:2}")  # space
print(f"{c:02}")

# ValueError: Invalid format specifier
# print(f"{c:*2}")
