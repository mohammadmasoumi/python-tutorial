a = int(input())
b = int(input())
c = int(input())

max_num = 0
mid_num = 0
min_num = 0

if a <= b <= c:
    max_num, mid_num, min_num = a, b, c
    # print(f"res: {a} <= {b} <= {c}")
elif a <= c <= b:
    # print(f"res: {a} <= {c} <= {b}")
elif b <= a <= c:
    # print(f"res: {b} <= {a} <= {c}")
elif b <= c <= a:
    # print(f"res: {b} <= {c} <= {a}")
elif c <= b <= a:
    # print(f"res: {c} <= {b} <= {a}")
elif c <= a <= b:
    # print(f"res: {c} <= {a} <= {b}")


print(f"res: {min_num} <= {mid_num} <= {max_num}")

# formatted string
# .format()

print("Hello", name, "'s", name, "How are you", name, )
print(f"Hello {name}'s name, How are you {name}")