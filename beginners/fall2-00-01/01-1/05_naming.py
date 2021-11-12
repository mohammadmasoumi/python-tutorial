# variable naming


"""
1. It must start with characters and underline/ underscore _
2. between meaningful strings we must use characters and numbers and underline/underscore
3. case sensitive - is sensitive to lower and upper case
"""

# 1

a = 12
_a = 12
B = 12
# 12a = 12
# *a = 12
# %a = 12


# 2
# variable name should be related to it's functionality
student_national_id = 410499722  # underline is allowed
# student national id = 410499722 - space is not allowed
# student-national-id = 410499722 - no dash
studentInationalIid = 410499722  # character is allowed
student1national1id = 410499722  # number is allowed

# 3

# two variables
x = 12
X = 13
ab = 12
aB = 13
AB = 12
Ab = 113
print(x, X)

# Convention - قرارداد
# snake case
student_national_id1 = 4141441414  # used in Python

# camel case
# first chunk starts with lowercase and the rest of chunks start with uppercase
studentNationalId = 4141441414

# pascal case
# first chunk and the rest of chunks start with uppercase
StudentNationalId = 4141441414
