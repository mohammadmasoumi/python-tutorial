"""
1. get the number of students

[
    [name, avg, cls, school],
    [name, avg, cls, school],
    [name, avg, cls, school]

]


"""
n = int(input())

students_info =    []

idx = 0
while idx < n:
    cls, school = input().split() # cls: "alef2", school: "estedadhaye darbodaghun"
    items = input().split() # ["hassan", "12", "20", "10"]
    name = items.pop(0)  # ["12", "20", "10"]

    sum_of_scores = 0
    for score in items:
        sum_of_scores += int(score)

    avg = sum_of_scores / len(items)
    students_info.append([name, avg, cls, school])

    idx += 1

name = input()
for info in students_info:
    # [name, avg, cls, school]
    if info[0] == name:
        print(info)
        break
