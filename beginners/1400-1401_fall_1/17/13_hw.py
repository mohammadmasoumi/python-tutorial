"""
10
A
B
C
D
A
B
C
D
E
"""

n = int(input())

"""
scores_dict : {
    "A": 1,
}
"""
scores_dict = {}
# scores_dict = {"A": 1}
# scores_dict = {"A": 2, "B": 1, "C": 1}

for idx in range(n):
    mark = input()  # mark = "A"
    #            scores_dict.get("A")
    mark_count = scores_dict.get(mark, 0)

    if mark_count == 0:  # add
        scores_dict[mark] = 1  # add key: "B" value: 1
    else:  # update
        mark_count += 1
        scores_dict[mark] = mark_count  # update

print(scores_dict)
