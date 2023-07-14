a = int(input())
b = int(input())

# 1.
if a > b:
    print(a)
else:
    print(b)

# 2.
# container
max = a
if b > max:
    max = b

print(max)
