"""
[Input]
4
mina 20 19 18 20 19 10 
asghar 10 11 20 10 20
behzad 20 19 10
hassan 20 19 10
asghar

[Output]
17.5
"""

# a, *b = [12, 13, 14]
# {
#   "mina": Student(),
#   "behzad": Student()
# }
data = {}

number_of_students = int(input())
counter = 0
while counter < number_of_students:
    # "mina 20 19 18 20 19 10"
    # name, scores = ["mina", "20", "19", "18", "20", "19" ,"10"]
    name, *scores = input().split()
    # name: "mina", scores: ["20", "19", "18", "20", "19" ,"10"]
    scores = list(map(int, scores))
    data[name] = f"{sum(scores) / len(scores):.2f}"

    counter += 1

name = input()
print(data[name])
