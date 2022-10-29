scores = [19.2, 16, 19.7, 14, 9]

index = 0

for score in scores:
    if score <= 18:
        scores[index] += 2
    else:
        scores[index] = 20

    index += 1

print(scores)