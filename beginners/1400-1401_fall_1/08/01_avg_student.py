n = int(input())

final_list = []
"""
4
ali 20 19 18
asghar 20 20 20
akbar 19 20 15
hassan 20 20 19 18
"""
for _ in range(n):

    # mohammad 20 19 18 17
    # ['mohammad', '20', '19', '18', '17']
    items = input().split()
    name = items[0]

    sum_scores = 0
    # len(items) = 5
    # ['20', '19', '18', '17']
    for idx in range(1, len(items)):
        sum_scores += int(items[idx])

    # [name, avg]
    # ['20', '19', '18', '17']
    # (len(items) - 1)=> numbers count
    final_list.append([name, sum_scores / (len(items) - 1)])

# input_name = input()

failed_list = []
for item in final_list:
    # ['ali', 18.5]
    # if item
    # print(item)
    # name, avg = ['ali', 18.5]
    name, avg = item
    if avg < 12:
        failed_list.append(item)
    # if name == input_name:
    #     print(avg)
    #     break

print(failed_list)
