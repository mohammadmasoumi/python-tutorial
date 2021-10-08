l = {}
first, second = 100, 100

for _ in range(int(input())):
    name = input()
    score = float(input())

    if score < first:
        first, second = score, first

    if first < score < second:
        second = score

    if l.get(score, []):
        l[score].append(name)
    else:
        l[score] = [name]

l2 = l[second]
l2.sort()

for item in l2:
    print(item)