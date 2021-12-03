"""

student count

name
last name
age
avg
is_male
"""

student_count = int(input())
students_data = {}

# double ctrl
# ctrl + down arrow
# ctrl + shift + right arrow
# ctrl + c

"""
[
    {
        "name: : "ali"
        "last_name: : "akbari"
        "age: : 20
        "avg: : 20
        "is_male: : True
    },
    {
        "name: : "hana"
        "last_name: : "hashemi"
        "age: : 21
        "avg: : 10.5
        "is_male: : False
    }
]

hana hashemi
{
    "name: : "hana"
    "last_name: : "hashemi"
    "age: : 21
    "avg: : 10.5
    "is_male: : False
}
"""

# [{} , {}]
for _ in range(student_count):
    name = input("name: ")
    last_name = input("last_name: ")
    age = int(input("age: "))
    avg = float(input("avg: "))
    is_male = bool(input("is_male: "))

    info = {
        'name': name,
        'last_name': last_name,
        'age': age,
        'avg': avg,
        'is_male': is_male,
    }
    key = f"{name} {last_name}"
    # students_data.update(key=info)
    students_data[key] = info
    print("-------------------------")

# student full name
full_name = input()

"""
{
    'hana hashemi': {     
        "name: : "hana"
        "last_name: : "hashemi"
        "age: : 21
        "avg: : 10.5
        "is_male: : False
    }, 
}
"""
print(students_data.get(full_name))
