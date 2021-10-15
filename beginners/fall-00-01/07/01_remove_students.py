"""
3
5
11
12
"""
number_scores = int(input())
my_scores = []

for idx in range(number_scores):
    score = int(input())

    if score > 20 or score < 0:
        print("Wrong input")
        break
    else:
        my_scores.append(score)

index = 0

my_scores_copy = my_scores.copy()
# my_scores_copy = list(my_scores)


# problem
# for item in my_scores:
#     print(f"index: {index}, item: {item}, len: {len(my_scores)}, scores: {my_scores}")
#
#     if item < 10:
#         my_scores.remove(item)
#         print(f"Removing index: {index}, item: {item}, len: {len(my_scores)}, scores: {my_scores}")
#
#     index += 1


# solution 1
for item in my_scores_copy:
    # print(f"index: {index}, item: {item}, len: {len(my_scores)}, scores: {my_scores}")

    if item < 10:
        my_scores.remove(item)
        # print(f"Removing index: {index}, item: {item}, len: {len(my_scores)}, scores: {my_scores}")

    index += 1


# solution 2
# erange(3)
# my_scores[0]
# [0, 1, 2]
# [4, 11, 12]

# for index in range(len(my_scores)):
#     # print(f"index: {index}, item: {item}, len: {len(my_scores)}, scores: {my_scores}")
#
#     # print(index)
#     if my_scores[index] < 10:
#         my_scores.remove(my_scores[index])
#         # print(f"Removing index: {index}, item: {item}, len: {len(my_scores)}, scores: {my_scores}")
#
#     # index += 1


print(my_scores)
