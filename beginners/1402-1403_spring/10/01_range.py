# built-in function

"""
int str float bool list
all any
print input
max min
sum 
len
isinstance
type
pow
chr ord
"""
# start, end, step
# list slice
# [start:end:step]

#   start: included
#   end: not included
#   step:
my_range = range(10, 50, 10) # iterable 
# iterable VS iterator

print(my_range) # range(10, 100, 10)
# [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(list(my_range))

print("--------------------")
for item in my_range:
    print(item)

print("--------------------")
for item in my_range:
    print(item)

"""
Application
    - generate sequence of numbers
        start end step
    range(10, 1000, 10)

    - generate indexes of a list -> range(10) -> [0, 1, 2, ..., 9]
    my_list = [1, 2, 3, 4]
    for idx in range(len(my_list)):
        print(my_list[idx])

    - repeat some action 
    for _ in range(3):
        input() 

    idx = 0
    while idx < 3:
        input()
        idx += 1
"""