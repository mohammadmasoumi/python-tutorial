
name = "ali"
grade = 19.2

# ali's mark is 19.2
print(name + "'s", "mark", "is", grade)
print(name + "'s mark is", grade)
print(f"{name}'s mark is {grade}")
print(f"{name}'s mark is {grade}")

# old fashion
print("{}'s mark is {}".format(name, grade))
print("{my_name}'s mark is {my_grade}".format(my_grade=grade, my_name=name))
#                                  0     1
print("{1}'s mark is {0}".format(name, grade))

