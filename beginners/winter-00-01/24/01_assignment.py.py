d = {}

for _ in range(int(input())):
    fname = input()
    lname = input()
    father_name = input()
    scores = list(map(int, input().split()))
    age = int(input())

    d[f"{fname}-{lname}-{father_name}"] = {
        "fname": fname,
        "lname": lname,
        "father_name": father_name,
        "scores": scores,
        "age": age,
        "avg": sum(scores) / len(scores),
        "max_score": max(scores),
        "min_score": min(scores),
        "has_less_than_10": bool(list(filter(lambda x: x<10, scores)))
    }
    # bool([10, 10]) => True
    # bool([])


winner = None
max_avg = -1
max_number = -1
min_number = 21
less_than_10_students = []

for student_key, student_data in d.items():

    if student_data.get("max_score") > max_number:
        max_number = student_data.get("max_score")

    if  min_number > student_data.get("min_score"):
        min_number = student_data.get("min_score")

    if student_data.get("has_less_than_10"):
        less_than_10_students.append(student_key)

    if student_data.get("avg") > max_avg:
        winner = student_key
        max_avg = student_data.get("avg")


print(f"min_score: {min_number}")
print(f"max_score: {max_number}")
print(f"less_than_10: {less_than_10_students}")
# "{fname}-{lname}-{father_name}"
# Asghar-Asghari-Akbar
print(f"winner: {' '.join(winner.split('-')[:2])}")
    







"""
{
    "ali asghari": {
        "fname": "ali",
        "lname": "asghari:.
        "father_name": "aliasghar",
        ...
    }
}




"""


"""
3
ali
asghari
20 20 20
19
max: 29

ali
asghari
20 20 20
19

"""
