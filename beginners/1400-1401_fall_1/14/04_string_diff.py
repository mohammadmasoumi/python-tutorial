"""
3
ali 20 20 19
hassan 19 10 12
asghar 12 17 19
asghar
"""
n = int(input())  # int("3")

my_students_avg = []
# my_students_avg: [["ali", 15], ["hassan", 17], ["asghar", 19]]
for i in range(n):
    # ["ali", "20", "20", "19"]
    scores = input().split()
    name = scores.pop(0)  # name: "ali", scores: ["20", "20", "19"]

    jam = 0
    for score in scores:
        # score: "20"
        jam += int(score)

    my_students_avg.append([name, jam / len(scores)])  # my_students_avg: [["ali", 59 / 3]]

candidate_name = input()

# for name_and_avg in my_students_avg:
for name, avg in my_students_avg:
    # name = name_and_avg[0]
    # avg = name_and_avg[1]
    if name == candidate_name:
        print(avg)
