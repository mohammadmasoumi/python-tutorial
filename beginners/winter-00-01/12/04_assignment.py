"""
3
---------------------
[ali 4]
    -------------
    Art 20
    PE 20
    Math 10
    Science 10
    -------------
---------------------
[hassan 4]
    -------------
    Art 20
    PE 20
    Math 10
    Science 10
    -------------
---------------------
[hossein 4]
    -------------
    Art 20
    PE 20
    Math 10
    Science 10
    -------------
--------------------
Math
"""

"""
[
    [name, [course, score], [course, score], [course, score], [course, score] ],
    [name, [course, score], [course, score], [course, score], [course, score] ], 
    [name, [course, score], [course, score], [course, score], [course, score] ] 
]
"""

# 1. 
n = int(input())

students_scores = []

for _ in range(n):
    # "ali 4"
    # items: ["ali", "4"]
    # name: "ali"
    # number_of_courses: "4"
    name, number_of_courses = input("Enter student and student course count: ").split()

    # student_scores: ["Ali", ["Art", 20], ["PE", 20]]
    student_scores = [name]
    
    for _ in range(int(number_of_courses)):
        course, score = input("Enter student course name and score: ").split()
        # "Art 20"
        # ["Art", "20"]
        # course, score = ["Art", "20"]
        # course, score = input().split()
        student_scores.append([course, int(score)])

    # students_scores: [
    #   ["Ali", ["Art", 20], ["PE", 20]]
    # ]
    students_scores.append(student_scores)

"""
[-
    [name, [course, score], [course, score], [course, score], [course, score] ],
    [name, [course, score], [course, score], [course, score], [course, score] ], 
    [name, [course, score], [course, score], [course, score], [course, score] ] 
]
"""
course = input("Enter the name of the course, you wanna get the AVG: ")

sum_score, count_score = 0, 0

for student_score in students_scores:
    # student_score: [name, [course, score], [course, score], [course, score], [course, score] ]

    for course_score in student_score[1:]:
        #                  0        1
        # course_score: [course, score]
        if course == course_score[0]:
            sum_score += course_score[1]
            count_score += 1


print(f"{course} avg: {sum_score / count_score}")


# for item1 in [1, 2]:
#     # code block
#     # item1: 1
#     for item2 in [3, 4]:
#         # code block
#         # item2: 3
#         # item2: 4
#         for item3 in [5, 6, 7]:
#             # code block
#             pass