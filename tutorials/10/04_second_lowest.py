n = int(input())

python_students = []

lowest_score = 101
second_lowest_score = 101

for _ in range(n):
    name = input()
    avg = float(input())

    if avg < lowest_score:
        lowest_score, second_lowest_score = avg, lowest_score

    if second_lowest_score > avg > lowest_score:
        second_lowest_score = avg

    python_students.append([name, avg])

second_lowest_students = []
for item in python_students:
    if item[1] == second_lowest_score:
        second_lowest_students.append(item[0])

print(second_lowest_students)