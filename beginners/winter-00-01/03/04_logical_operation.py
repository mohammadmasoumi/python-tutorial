a = 10
b = 11
c = 12

# b > a and c > b
# and - و
# TRUE and TRUE = True
# True and False = False
# False and TRUE = Flase
# False and False = False

# or - یا
# True or True = True
# True or False = True
# False or True = True
# False or False = False

# not 
# not True = False
# not False = True

# print(b > a and c > b and 1 == 1 or ...)
print(b > a and c > b and 1 == 1)
print((b > a and c > a) or (c > a and b > a))
# (True and c > a) or (c > a and b > a)
# (True and True) or (c > a and b > a)
# True or (c > a and b > a)
# ...