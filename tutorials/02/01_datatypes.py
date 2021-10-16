# declaring data-types


# int
a1 = 12
a2 = int(12)
a3 = int('12')  # casting
a4 = int(12.0)
a5 = int(True)

print(f"a1: {a1}, type a1: {type(a1)}")
print(f"a2: {a2}, type a2: {type(a2)}")
print(f"a3: {a3}, type a3: {type(a3)}")
print(f"a4: {a4}, type a4: {type(a4)}")
print(f"a5: {a5}, type a5: {type(a5)}")
print("-----------------------------------------")

# float
b1 = 12.0
b2 = float(12.1)
b3 = float('12.1')  # casting
b4 = float(12)
b5 = float(True)

print(f"b1: {b1}, type b1: {type(b1)}")
print(f"b2: {b2}, type b2: {type(b2)}")
print(f"b3: {b3}, type b3: {type(b3)}")
print(f"b4: {b4}, type b4: {type(b4)}")
print(f"b5: {b5}, type b5: {type(b5)}")
print("-----------------------------------------")

# str
c1 = "12"
c2 = str("12")
c3 = str(12)
c4 = str(12.2)
c5 = str(True)

print(f"c1: {c1}, type c1: {type(c1)}")
print(f"c2: {c2}, type c2: {type(c2)}")
print(f"c3: {c3}, type c3: {type(c3)}")
print(f"c4: {c4}, type c4: {type(c4)}")
print(f"c5: {c5}, type c5: {type(c5)}")
print("-----------------------------------------")

# bool

d1 = True
d2 = bool("12")
d3 = bool(12)
d4 = bool(12.2)
d5 = bool(True)

# False values
d6 = bool(False)  # False
d7 = bool("")  # False
d8 = bool(0)  # False
d9 = bool(0.0)  # False
d10 = bool([])  # False

print(f"d1: {d1}, type d1: {type(d1)}")
print(f"d2: {d2}, type d2: {type(d2)}")
print(f"d3: {d3}, type d3: {type(d3)}")
print(f"d4: {d4}, type d4: {type(d4)}")
print(f"d5: {d5}, type d5: {type(d5)}")
print("-----------------------------------------")

# list
e1 = []
e2 = list([1, "Hello", True, 1.0, [1, 2]])
e3 = list("string")
# e3 = list(12)  # TypeError: 'int' object is not iterable
# e4 = list(12.2)  # TypeError: 'float' object is not iterable
# e5 = list(True)  # TypeError: 'float' object is not iterable

print(f"e1: {e1}, type e1: {type(e1)}")
print(f"e2: {e2}, type e2: {type(e2)}")
print(f"e3: {e3}, type e3: {type(e3)}")
print("-----------------------------------------")
