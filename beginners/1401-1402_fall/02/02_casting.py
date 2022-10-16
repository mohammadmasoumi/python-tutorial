# Cast
# type -> type

# built-in function
# print
# int
# str
# float
# bool

a = 12
a1 = str(a) # int -> str ('12' "12")
a2 = float(a) # int -> float 12.0
a3 = bool(a) # int -> bool True [True, False, Exception]
a4 = bool(-12) # True
a5 = bool(1) # True
a6 = bool(0) # False

"""
int 
truthy -> (-oo, +oo) except ZERO 
falsey -> 0
"""

print(f"a1: {a1}, type(a1): {type(a1)}")
print(f"a2: {a2}, type(a2): {type(a2)}")
print(f"a3: {a3}, type(a3): {type(a3)}")
print(f"a4: {a4}, type(a4): {type(a4)}")
print(f"a5: {a5}, type(a5): {type(a5)}")
print(f"a6: {a6}, type(a6): {type(a6)}")

print("----------------------------------------------")

b = ''
b1 = '12'
b2 = "ali"
b3 = int(b1) # str -> int ('12' -> 12)
# b4 = int(b2) # str -> int ("ali" -> 657074) Exception
b5 = float(b1) # str -> float ('12' -> 12.0)
# b6 = float(b2) # str -> float ('ali' -> 657074.0)
b7 = bool(b) # str -> bool ('' -> (False, True)) False
b8 = bool(b1) # str -> bool () True
b9 = bool(b2) # str -> bool () True
b10 = str(b) # str -> str
b11 = str(b1) # str -> str
b12 = str(b2) # str -> str
b13 = int("          12") # strip
# b14 = int("12******")
b15 = int("12         ")
# b16 = int("1         2")

"""
str 
truthy -> None other than '' 
falsey -> ''
"""

print(f"b: {b}, type(b): {type(b)}")
print(f"b1: {b1}, type(b1): {type(b1)}")
print(f"b2: {b2}, type(b2): {type(b2)}")
print(f"b3: {b3}, type(b3): {type(b3)}")
# print(f"b4: {b4}, type(b4): {type(b4)}")
print(f"b5: {b5}, type(b5): {type(b5)}")
# print(f"b6: {b6}, type(b6): {type(b6)}")
print(f"b7: {b7}, type(b7): {type(b7)}")
print(f"b8: {b8}, type(b8): {type(b8)}")
print(f"b9: {b9}, type(b9): {type(b9)}")
print(f"b10 {b10}, type(b10): {type(b10)}")
print(f"b11 {b11}, type(b11): {type(b11)}")
print(f"b12 {b12}, type(b12): {type(b12)}")
print(f"b13 {b13}, type(b13): {type(b13)}")
# print(f"b14 {b14}, type(b14): {type(b14)}")
print(f"b15 {b15}, type(b15): {type(b15)}")
# print(f"b16 {b16}, type(b16): {type(b16)}")

print("----------------------------------------------")

c1 = 12.3 
c2 = str(c1) # ('12.3')  '12'  '0.3'
c3 = int(c1) # (12) 123 3 
c4 = bool(c1) # True
c5 = bool(0.0) # True (False)
c6 = bool(-0.1) # True
c7 = int(12.0) # 12
c8 = int(12.9) # 12

"""
float 
truthy -> (-oo, +oo) except 0.0 
falsey -> 0.0
"""

print(f"c1: {c1}, type(c1): {type(c1)}")
print(f"c2: {c2}, type(c2): {type(c2)}")
print(f"c3: {c3}, type(c3): {type(c3)}")
print(f"c4: {c4}, type(c4): {type(c4)}")
print(f"c5: {c5}, type(c5): {type(c5)}")
print(f"c6: {c6}, type(c6): {type(c6)}")
print(f"c7: {c7}, type(c7): {type(c7)}")
print(f"c8: {c8}, type(c8): {type(c8)}")

print("----------------------------------------------")

d1 = True
d2 = False
d3 = int(d1) # 0 -1 Exception True (1)   
d4 = int(d2) # (0) -1 Exception
d5 = float(d1) # 1.0
d6 = float(d2) # 0.0
d7 = str(d1) # 'True'
d8 = str(d2) # 'False'
d9 = bool(d1) # True
d10 = bool(d2) # False

print(f"d1: {d1}, type(d1): {type(d1)}")
print(f"d2: {d2}, type(d2): {type(d2)}")
print(f"d3: {d3}, type(d3): {type(d3)}")
print(f"d4: {d4}, type(d4): {type(d4)}")
print(f"d5: {d5}, type(d5): {type(d5)}")
print(f"d6: {d6}, type(d6): {type(d6)}")
print(f"d7: {d7}, type(d7): {type(d7)}")
print(f"d8: {d8}, type(d8): {type(d8)}")
print(f"d9: {d9}, type(d9): {type(d9)}")
print(f"d10: {d10}, type(d10): {type(d10)}")


# list
"""
list 
truthy -> none other than [] 
falsey -> []
"""