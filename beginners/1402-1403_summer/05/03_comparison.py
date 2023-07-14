a = int(input())
b = int(input())
c = int(input())

# ctrl + shift + alt + top/bot arrow

# 1
if a < b < c:
    print(f"{a}<{b}<{c}")
elif a < c < b:
    print(f"{a}<{c}<{b}")
elif b < a < c:
    print(f"{b}<{a}<{c}")
elif b < c < a:
    print(f"{b}<{c}<{a}")
elif c < a < b:
    print(f"{c}<{a}<{b}")
elif c < b < a:
    print(f"{c}<{b}<{a}")

# 2
min = a
avg = b
max = c

if a < b < c:
    min = a
    avg = b
    max = c
elif a < c < b:
    min = a
    avg = c
    max = b
elif b < a < c:
    min = b
    avg = a
    max = c
elif b < c < a:
    min = b
    avg = c
    max = a
elif c < a < b:
    min = c
    avg = a
    max = b
elif c < b < a:
    min = c
    avg = b
    max = a

print(f"{min}<{avg}<{max}")

# 3
if a < b < c:
    min, avg, max = a, b, c
elif a < c < b:
    min = a
    avg = c
    max = b
elif b < a < c:
    min = b
    avg = a
    max = c
elif b < c < a:
    min = b
    avg = c
    max = a
elif c < a < b:
    min = c
    avg = a
    max = b
elif c < b < a:
    min = c
    avg = b
    max = a

print(f"{min}<{avg}<{max}")
