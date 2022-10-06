

"""
n=3

Ali 20 19 20
Hassan 20 19 17
Mobina 19 18 10


# Final answer

Ali 19.2
Hassan 19.2
Mobina 19.2
"""



name_scores = []


n = int(input())


for _ in range(n):
    items = input().split()

    name_scores.append(items)


for items in name_scores:
    name = items.pop(0)

    sum = 0
    for item in items:
        sum += int(item)

    avg = sum / len(items)
    
    print(f"{name} {avg}")
