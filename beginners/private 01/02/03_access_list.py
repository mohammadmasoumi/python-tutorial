# my_list = [[1, 2], [3, 4] , [5, 6]]
# print(my_list[0][1])

fruits = ["orange", "banana", "peach", "apricot", "watermelon", "cucumber", "apple"]

# acess to the element
print(fruits[0]) # single elemnet
print(fruits[0:1]) # multiple elmenets 

# ["peach", "apricot", "watermelon"]
print(fruits[2:5][0:2])

# colon :
print(fruits[-5::-1]) # ["peach", "banana", "orange"]
print(fruits[::-1]) # reverse
print(fruits[:-5:-1])
print(fruits[:-5:1])
print(fruits[-5:-2:-1])
print(fruits[-2:-5:-1])
print(fruits[-5:-2:1])
print(fruits[3:3]) # []
print(fruits[::3])

# ["orange", "peach", "cucumber", "apple"]
print(fruits[:3:2] + fruits[-2:])

# fruits = ["orange", "banana", "peach", "apricot", "watermelon", "cucumber", "apple"]
# ["orange", "cucumber", "watermelon", "peach", "apricot", "banana",  "apple"]
print(fruits[::5] + fruits[-3:-6:-2] + fruits[3:0:-2] + fruits[-1:])
# TypeError: can only concatenate list (not "str") to list
# print(fruits[::5] + fruits[-3:-6:-2] + fruits[3:0:-2] + fruits[-1]) # [] + "apple"


# list
#     access
#           index
#           range index
#     add
#           append
#           extend
#           insert
#     update
#           update
#     remove
#           remove
#           pop
#     
