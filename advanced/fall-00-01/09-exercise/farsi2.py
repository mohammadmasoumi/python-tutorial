number = int(input("please insert the number of students :\n"))
x = 1
minimum = 999999999999999999
list = []
while number >= x:
    students = input("please insert their names with their mark : \n").split()
    for d in students:
        name = students.pop(0)
        name = str(name)
        mark = students.pop()
        mark = int(mark)
        list.append(name)
        list.insert(1, mark)
        print(list)

    for i in list:
        if list[1] < minimum:
            minimum = list[1]

    x += 1

print("\n\n------------------------------------\n\n")
print(f"the the minimum mark is {minimum}\n\n")