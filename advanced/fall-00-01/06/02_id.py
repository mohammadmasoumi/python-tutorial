# immutable

a = 12
b = 12
a1 = int(a)

c1 = "a"
c2 = f"{c1}"

print(id(c1))
print(id(c2))

# 0x7ffdfff60810
# print(hex(id(a)))
# print(hex(id(b)))
# print(hex(id(b)))
# print(bin(12))
# hex() مبنای 16
# oct() مبنای 8
# bin() مبنای 2
print(id(a))
print(id(b))
print(id(a1))

# --------------------------------
my_list1 = [1, 2]
my_list2 = [1, 2]
my_list3 = my_list2
my_list4 = my_list2.copy()

print(my_list2)
print(my_list3)
print(my_list4)
my_list2.append(10)
print(my_list2)
print(my_list3)
print(my_list4)

print(f"my_list1: {hex(id(my_list1))}")
print(f"my_list2: {hex(id(my_list2))}")
print(f"my_list3: {hex(id(my_list3))}")
print(f"my_list4: {hex(id(my_list4))}")

# ----------------------------
print("-----------------------------------------")

a = 20
b = 21

my_list12 = [a, b]
my_list22 = [a, b]

print(id(a))
print(id(b))

for item in my_list12:
    print(id(item))

for item in my_list22:
    print(id(item))
