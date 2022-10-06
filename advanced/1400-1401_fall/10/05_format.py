# ValueError: Format specifier missing precision
r = 10
print(f"{12.0000:5.10f}             {10:10.20f}")
print(f"{12.0:.8f}")

# ---------------------------------                                                                                                12.00
print(f"{12.0:100.2f}")
print(f"{12.0:3.8f}")

# ---------------------------------
print(f"{12.2:f}")  # float
print(f"{12:o}")  # octal
print(f"{12:X}")  # hexadecimal
print(f"{12:b}")  # binary

# print("Abulfadl Ahmadi")
