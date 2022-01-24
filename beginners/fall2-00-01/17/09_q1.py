# store all name, avg of students
student_avg = {
    "ali": 20,
    "hassan": 10,
    "mina": 20,
    "ali": 19 # the value of "ali" will be 19
}

#print(student_avg)
#print(student_avg["ali"])
# ------------------------
student_data = [
    {
        "name": "ali",
        "avg": 20,
        "age": 30
    },
    {
        "name": "hassan",
        "avg": 20
    },
    {
        "name": "hassan",
        "avg": 10
    }
]

for item in student_data:
    # type(item): dict
    # item = {
    #    "name": "hassan",
    #    "avg": 10
    #}
    # print(item.get("name"), item.get("avg"), item.get("age", 20))
    if item.get("name") == "hassan":
        print(item.get("name"), item.get("avg"), item.get("age", 20))

    # if item.get("avg") > 10:
    # if item.get("age") > 18: