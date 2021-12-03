"""

student count

name
last name
age
avg
is_male
"""

student_count = int(input())
students_data = []

# double ctrl
# ctrl + down arrow
# ctrl + shift + right arrow
# ctrl + c
"""
2
name: ali
last_name: alavi
age: 20
avg: 20
is_male: 1
-------------------------
name: hana
last_name: hashemi
age: 21
avg: 10
is_male: 0
-------------------------
hana hashemi
{'name': 'hana', 'last_name': 'hashemi', 'age': 21, 'avg': 10.0, 'is_male': True}
"""
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
    students_data.append(info)
    print("-------------------------")

# student full name
full_name = input()

name, last_name = full_name.split()

for item in students_data:
    if item.get('name') == name and item.get('last_name') == last_name:
        print(item)
