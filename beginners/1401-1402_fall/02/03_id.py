# ID - unique identifier
from copy import deepcopy

a = 12
b = a

print(f"a: {a}, id(a): {id(a)}")
print(f"b: {b}, id(b): {id(b)}")
print("---------------------")

a = 1200
b = a

print(f"a: {a}, id(a): {id(a)}")
print(f"b: {b}, id(b): {id(b)}")
print("---------------------")

a = 12
b = 12

print(f"a: {a}, id(a): {id(a)}")
print(f"b: {b}, id(b): {id(b)}")
print("---------------------")

a = [12, 13]
b = [12, 13]

print(f"a: {a}, id(a): {id(a)}")
print(f"b: {b}, id(b): {id(b)}")
print(f"a[0]: {a[0]}, id(a[0]): {id(a[0])}")
print(f"b[0]: {b[0]}, id(b[0]): {id(b[0])}")
print("---------------------")

a = [12, 13]
b = a

print(f"a: {a}, id(a): {id(a)}")
print(f"b: {b}, id(b): {id(b)}")
print(f"a[0]: {a[0]}, id(a[0]): {id(a[0])}")
print(f"b[0]: {b[0]}, id(b[0]): {id(b[0])}")
print("---------------------")

a = [12, 13]
b = a.copy()

print(f"a: {a}, id(a): {id(a)}")
print(f"b: {b}, id(b): {id(b)}")
print(f"a[0]: {a[0]}, id(a[0]): {id(a[0])}")
print(f"b[0]: {b[0]}, id(b[0]): {id(b[0])}")
print("---------------------")

a = [[12, 13]]
b = a.copy()

print(f"a: {a}, id(a): {id(a)}")
print(f"b: {b}, id(b): {id(b)}")
print(f"a[0]: {a[0]}, id(a[0]): {id(a[0])}")
print(f"b[0]: {b[0]}, id(b[0]): {id(b[0])}")
print("---------------------")

a = [[12, 13]]
b = deepcopy(a)

print(f"a: {a}, id(a): {id(a)}")
print(f"b: {b}, id(b): {id(b)}")
print(f"a[0]: {a[0]}, id(a[0]): {id(a[0])}")
print(f"b[0]: {b[0]}, id(b[0]): {id(b[0])}")
print("---------------------")
