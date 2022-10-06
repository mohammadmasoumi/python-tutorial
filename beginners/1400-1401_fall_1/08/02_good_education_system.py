n = int(input())

final_list = []

# n = 5
for _ in range(n):
    # score = 10
    score = int(input())

    if 17 <= score <= 20:
        score = 'A'
    elif 14 <= score < 17:
        score = "B"
    elif 11 <= score < 14:
        score = "C"
    elif 8 <= score < 11:
        score = 'D'
    else:
        score = 'E'

    # final_list = [['A', 1], ['C', 2]]
    # score = 'D'

    # باید تعداد نمرات را بشمارم.
    # for item in final_list:
    #     # ['A', 1]
    #     s, count = item
    #     if s == score:
    #         count += 1
    #                   0         1
    # final_list = [['A', 1], ['B', 2]]
    # final_list = []

    # final_list = [['A', 1], ['C', 2]]
    # score = 'D'
    for idx in range(len(final_list)):
        # idx = 1
        # item =  ['C', 2]
        item = final_list[idx]
        # s = 'C'
        # count = 2
        s, count = item

        if score == s:
            count += 1  # count = 2
            # score = 'C', count = 2
            # [score, count]
            final_list[idx] = [score, count]
            # final_list = [['A', 1], ['C', 2]]
            break
    else:
        # score = 'D'
        final_list.append([score, 1])
        # final_list = [['A', 1], ['C', 2], ['D', 1]]

print(final_list)
