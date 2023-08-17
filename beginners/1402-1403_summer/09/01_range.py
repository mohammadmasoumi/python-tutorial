
# range 

# builtin function

"""
slice 

start: included
end: not included

[start:end:step]
[:end:step]

----
range(end)
range(start, end)
range(start, end, step)

           <-step->
start                   end
end                     start

"""

# end: 10 
# start: 0
# step: 1
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10)))

# start: 2
# end: 10
# step: 1
# [2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(2, 10)))

# start: 2
# end: 10
# step: 4
# [2, 6]
print(list(range(2, 10, 4)))

# start: 10
# end: 2
# step: -2
# [10, 8, 6, 4]
print(list(range(10, 2, -2)))

# end
# [1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
print(list(range(1,-10,-1)))