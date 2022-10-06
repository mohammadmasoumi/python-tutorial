
count = int(input())
student_scores = []

for _ in range(count):
    # scores: ["Ali", "20", "19", "18"]
    scores = input().split()
    name = scores.pop(0)

    # if we are sure all scores are between 0 and 20
    avg = sum(map(int, scores)) / len(scores)

    # if we want to make sure that all scores are between 0 and 20
    # sum_of_scores = 0
    # score_counts = 0
    # for score in scores:
    #    score = int(score)

    #    if 0 <= score <= 20:
    #        sum_of_scores += score
    #        score_counts += 1

    # avg = sum_of_scores / score_counts
    # student_scores.append([name, avg])


print(student_scores)