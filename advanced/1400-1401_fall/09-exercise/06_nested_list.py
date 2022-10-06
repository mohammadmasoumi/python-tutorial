stu_num = int(input())

lower = 101
se_lower = 101

final_list = []
students = []

lower_names = []
second_lower_names = []

for _ in range(stu_num):
    name = input()
    mark = float(input())

    if mark <= lower:
        se_lower = lower
        lower = mark

        lower_names.append(name)
        if lower == se_lower:
            second_lower_names = lower_names.copy()
            lower_names.clear()

    if lower < mark < se_lower:
        se_lower = mark
        second_lower_names.append(name)

    # students.append([name, mark])

# for name, score in students:
#     if score == se_lower:
#         final_list.append(name)

second_lower_names.sort()
for item in second_lower_names:
    print(item)
