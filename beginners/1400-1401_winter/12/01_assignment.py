"""
5
ali 20 20 18
hassan 12 10 11
hossein 10 16 12
mohammad 2 10 20
asghar 20 10 19
--------------------
ali 19
hassan 10
hossein 13
mohammad 10
asghar 15
"""

"""
1. get number from user
2. get name and marks from user
list: []
    [[], [], [], []]
    [[[]. []], [[], []], [[], []], [[], []]]
3. cast all str scores to int scores

"""

# 1.
n = int(input()) # type(n) ?

# n = int(n)
# print(n , type(n))

# 2.
name_avg = []

for _ in range(n):
    item = input()
    # "ali 20 20 19"
    # print(list(item))
    # ['a', 'l', 'i', ' ', '2', '0', ' ', '2', '0', ' ', '1', '9']
    items = item.split()
    # ['ali', '20', '20', '19']
    name, *scores = items
    
    # name: 'ali' scores: ['20', '20', '19']
    # 3.
    for idx, score in enumerate(scores):
    # print(idx, item)
        scores[idx] = int(score)

    # print(sum(items[1:]))
    avg = sum(scores) / len(scores)
    
    # [['ali', 19], ['hassan', 18], []]
    # ['ali', 19, 'hassan', 18]
    name_avg.append([name, avg])

    # print(sum(scores) )
    # print(item)

