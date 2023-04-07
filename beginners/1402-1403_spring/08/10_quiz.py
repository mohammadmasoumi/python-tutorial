scores = [20, 20, 20, 20]
scores = [20, 20, 20, 10]
scores = [10, 10, 10, 10]


"""
all 20 -> Bravo
all 10 -> Awful
else ->  Try more
"""

twenty_scores = 0
less_than_ten_scores = 0

for score in scores:
    if score == 20:
        twenty_scores += 1
    elif score <= 10:
        less_than_ten_scores += 1
    
if twenty_scores == len(scores):
    print("Bravo")
elif less_than_ten_scores  == len(scores):
    print("awful")
else:
    print("Try more")