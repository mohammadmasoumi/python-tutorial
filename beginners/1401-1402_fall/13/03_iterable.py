# built-in
my_list = [1, 2, 3, 4]

def function(x):
    return x % 2

# b = list(filter(function, my_list))
b = filter(function, my_list)

d = b

for item in b:
    print(item)

print("--------------")
for item in b:
    print(item)

print("--------------")
c = b
for item in c:
    print(item)

print("--------------")
for item in d:
    print(item)

print("**********************************")
my_list = [1, 2, 3, 4, 5, 6, 7, 8]

def function(x):
    return x % 2

# b = list(filter(function, my_list))
my_new_list = filter(function, my_list)
# [1, 2, 3, 4]
# next(my_new_list) 1
# next(my_new_list) 2
print(next(my_new_list))
print("---------------------------")
for item in my_new_list:
    print(item)

# StopIteration
print(next(my_new_list))