scores = [18, 18, 19, 19, 2, 10]

min = 20
second_min = 20

for score in scores:
    if score < min:
        second_min = min
        min = score

    elif min < score < second_min:
        second_min = score

print(second_min)