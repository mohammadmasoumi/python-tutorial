d = {}

# : unsupported operand type(s) for +: 'int' and 'str'
# TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
# TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
# print(sum(int(("20", "10", "20"))))
print(sum((20, 10, 20)))

for _ in range(int(input())):
    name, *marks = input().split()
    d[name] = sum(list(map(int, marks))) // len(marks)

print(d)
