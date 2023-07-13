# fstring 3.6

# format

name = "Tom"
age = 2

print("Hello {}, I am {} year(s) old".format(name, age))
#                                              0    1
#                                           [name, age]
print("Hello {1}, I am {0} year(s) old".format(name, age))
print("Hello {1}, I am {0} year(s) old".format("Tom", 2))

# keyword argument
#              key             key                    key=value
print("Hello {name1}, I am {age1} year(s) old".format(age1=age, name1=name))
print("Hello {name1}, I am {age1} year(s) old".format(age1=2, name1="Tom"))
print("Hello {name}, I am {age} year(s) old".format(age=age, name=name))
print("Hello Tom, I am 2 year(s) old")
