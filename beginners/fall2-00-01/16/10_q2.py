student_data1 = [
    {
        "name": "ali",
        "avg": 20,
        "age": 30,
        "national_id": "1234"
    },
    {
        "name": "hassan",
        "avg": 20,
        "national_id": "1236"
    },
    {
        "name": "hassan",
        "avg": 10,
        "national_id": "1235"
    }
]

student_data2 = {
    "1234": {
        "name": "ali",
        "avg": 20,
        "age": 30,
        "national_id": "1234"
    },
    "1236": {
        "name": "hassan",
        "avg": 20,
        "national_id": "1236"
    },
     "1235": {
        "name": "hassan",
        "avg": 10,
        "national_id": "1235"
    }
}

national_id = "1234"
print(student_data2)
print(student_data2.get(national_id))