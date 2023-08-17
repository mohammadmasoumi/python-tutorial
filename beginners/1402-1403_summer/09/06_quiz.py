"""
scores = [20, 19, 18, 10]

17 20 -> A
14 17 -> B
11 14 -> C
8 11 -> D
<8 -> E
"""

#          0   1   2
scores = [20, 19, 18, 2, 8, 4, 9, 11, 15, 16]
#       ["A", "A", "A", ...]

for idx, item in enumerate(scores):
    # item: scores[idx]
    # value of `idx` index: scores[idx]
    if 17 < item <= 20:
        scores[idx] = "A"
    elif 14 < scores[idx] <= 17:
        scores[idx] = "B"
    elif 11 < item <= 14:
        scores[idx] = "C"
    elif 11 < item <= 14:
        scores[idx] = "D"
    else:
        scores[idx] = "E"

print(scores)
        