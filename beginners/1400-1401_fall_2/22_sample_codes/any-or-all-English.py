numbers = input().split()
print(any(map(lambda x: x[0: len(x)//2] == x[len(x)//2 + 1: len(x)] or len(x) == 1,numbers)) and all(map(lambda x: int(x) == abs(int(x)), numbers)))