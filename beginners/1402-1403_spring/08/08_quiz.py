scores = [2, 7, 8, 8, 19.75, 9, 5]
scores = [18, 18, 19, 19, 2, 10]

max = 0 # 10
second_max = 0 # 8

# [10, 8, 12]

# max: 12
# second_max: 10

for score in scores:

    if score > max:
        second_max = max
        max = score

    elif second_max < score < max:
        second_max = score

print(second_max)