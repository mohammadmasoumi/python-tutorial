scores = [9.75, 8, 6.5, 2, 3]

idx = 0 
for score in scores:
    score = score * 3 + 5
    
    # if score > 20:
    #     score = 20
    # scores[idx] = score

    scores[idx] = min(20, score) # max
    idx += 1

print(scores)

