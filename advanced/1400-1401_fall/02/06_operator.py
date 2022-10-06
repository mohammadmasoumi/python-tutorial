# operator

# arithmetic operator

a = 12 + 12
b = 12 - 12
c = 12 * 12
d = 12 / 12
e = 12 ** 2  # power
f = 12 // 5  # اعشارش را می اندازد
g = 13 % 5

print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")
print(f"e: {e}")
print(f"f: {f}")
print(f"g: {g}")

# assignment operator

a1 = 12
a1 += 12
a1 -= 12
a1 *= 12
a1 /= 12
a1 //= 12
a1 **= 12

b1 = 12
c1 = 0

# bitwise operator
print(f"b1 | c1: {b1 | c1}")
print(f"b1 & c1: {b1 & c1}")
print(f"b1 ^ c1: {b1 ^ c1}")
print(f"~b1: {~b1}")

print(f"oct(12): {oct(12)}")
print(f"hex(12): {hex(12)}")

# comparison
print(f"== {12 == 12}")
print(f"!= {12 != 12}")
print(f">= {12 >= 12}")
print(f"<= {12 <= 12}")
print(f"< {12 < 12}")
print(f"> {12 > 12}")

# logical
aTrue = True
aFalse = False
print(f"and: {aTrue and aFalse}")
print(f"or: {aFalse or aTrue}")
print(f"not: {not aFalse}")

# identity
arr1 = []
arr2 = []
arr3 = arr1

print(f"arr1: {id(arr1)}")
print(f"arr2: {id(arr2)}")
print(f"arr3: {id(arr3)}")

print(f"{arr1 is arr3}")
print(f"{arr3 is arr1}")
print(f"{arr1 is not arr2}")

# z1 = 12
# z2 = z1
# z3 = 12

z1 = [1, 2]
z2 = z1
z3 = [1, 2]

print("-----------------------------------")
print(f"{z1 is z3}")
print(f"{z1 == z3}")
# print("")

# membership operator

arr = [1, 2, 3]
arr1 = [[3, 4], 1, 2]

print(f"membership: {1 in arr}")
print(f"membership: {4 not in arr}")
print(f"membership: {3 in arr1}")
print(f"membership: {3 in arr1[0]}")
