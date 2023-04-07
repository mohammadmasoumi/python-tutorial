scores = [2, 7, 8, 9.75, 9, 5]

# print(min(scores), max(scores), sum(scores)/len(scores))

min_score = scores[0] # 20 max sample space
max_score = scores[0] # 0 min sample space
sum = 0

for score in scores:
    if score < min_score:
        min_score = score

    if score > max_score:
        max_score = score

    sum += score

print(min_score, max_score, sum / len(scores))
