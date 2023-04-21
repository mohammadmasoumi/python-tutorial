"""
3
MrJadidi 10 10 10
MrImani 10 12 8
MrSalmanPour 9 9 9 9

? GooD Student
"""

"""
1. get number of students
2. get student's scores: MrJadidi 10 10 10
3. calc avg student's
4. get the max avg
5. print max avg student
"""

n = int(input()) # [1]
idx = 0 

max_avg_so_far = 0
max_avg_so_far_name = ""

while idx < n :
    items = input().split() # [2] items: ["MrJadidi", "10", "10", "10"]
    name = items.pop(0) # items: ["10", "10", "10"]

    sum_scores = 0
    for score in items:
        sum_scores += int(score)
    
    avg = sum_scores / len(items)

    if avg > max_avg_so_far:
        max_avg_so_far = avg
        max_avg_so_far_name = name

    idx += 1

print(max_avg_so_far, max_avg_so_far_name)