
scores = [10, 20, 20, 20]

if not scores:
    print("List is empty")
else:
    # current_max = scores[0]
    current_max = scores[0] if scores else 0 
    current_min = scores[0] if scores else 20 

    for score in scores:

        if score < current_min:
            current_min = score
        
        if  current_max < score:
            current_max = score

    print(current_max, current_min)

print(max(scores), min(scores))