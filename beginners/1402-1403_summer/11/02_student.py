students = [] 
for _ in range(int(input())):
    items = input().split()
    name = items.pop(0)
    
    s = 0
    for score in items:
        s += int(score)

    avg = s / len(items)
    students.append([name, avg])

std_name = input()
for name, avg in students: 
    if name == std_name:
        print(avg)
