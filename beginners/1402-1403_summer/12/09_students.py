n = int(input())

for _ in range(n):
    items = input().split() # ["ali", "20", "19"]
    name = items.pop(0)
    scores = list(map(int, items)) # scores: [20, 19]
    avg = sum(scores) / len(scores)

    # C, java, ...
    # s = 0
    # for score in scores:
    #     s += int(score)
    # s / len(scores)

my_list = []
my_list.get