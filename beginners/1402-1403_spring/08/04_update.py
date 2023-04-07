
scores = [9.75, 8, 6.5, 2, 3]

# +8
idx = 0
for score in scores:
    # score: float | immutable
    # score = score + 8
    # [17.75, 8, 6.5, 2, 3]
    # [16, 8, 6.5, 2, 3]
    # [14.5, 8, 6.5, 2, 3]
    # [10, 8, 6.5, 2, 3]
    # [11, 8, 6.5, 2, 3]
    score += 8
    # scores[0] = score
    # print(scores[0])
    scores[idx] = score
    idx += 1

print(scores)
