# input

# one input on each line
# if you need an int do not forget to cast it.
str_input = input()  # the type of n is str

print(str_input)
print(type(str_input))

int_input = int(input())
print(int_input)
print(type(int_input))

# input in one-line
"""
How we can get input in one line from user?

input:
1 2 3 4 5

output: print(a_list)
['1', '2', '3', '4', '5']  # a_list
"""
a_list = input().split()
print(a_list)

# be aware each element is string
# ['1', '2', '3', '4', '5']
