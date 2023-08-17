# slice/slicing 

"""
slice[start:end:step]

start (included) 
end (not included)
step (+/- + left to right | - right to left)
"""
# positive 0  1  2  3  4  5  6
# negative-7 -6 -5 -4 -3 -2 -1
my_list = [1, 2, 3, 4, 5, 6, 7]

# start: 0
# end: 2
# step: +1 (default) 
print(my_list[0:2]) # values: [1, 2]
print(my_list[0: 4: 2]) # [1, 3]

print(my_list[-6:2:3]) # [2]
# start: -1
# end: -6
# step: 1
print(my_list[-1:-6]) # []
print(my_list[-1:-6:-1]) # [7, 6, 5, 4, 3]
print(my_list[-1:-6:-3]) # [7, 4]
# -> 4
print(my_list[:4]) # [1, 2, 3, 4]
#    4 <-
print(my_list[:4:-1]) # [7, 6]
#   <- 2
print(my_list[2::-1]) # [3, 2, 1]

print(my_list[::-1]) # reverse list [7, 6, 5, 4, 3, 2, 1]
print(my_list[::2]) # [1, 3, 5, 7]