d = {}
for _ in range(int(input())):
    name, *scores = input().split()
    d[name] = sum(map(int, scores)) // len(scores)

print(d.get(input(), "Not found"))