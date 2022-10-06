args = input().split()

a, b, c = int(args[0]), int(args[1]), int(args[2])

if a > b > c:
    print(f"{a} > {b} > {c}")
elif a > c > b:
    print(f"{a} > {c} > {b}")
elif b > a > c:
    print(f"{b} > {a} > {c}")
elif b > c > a:
    print(f"{b} > {c} > {a}")
elif c > a > b:
    print(f"{c} > {a} > {b}")
else:
    print(f"{c} > {b} > {a}")
