"""
12 13 14 15
"""

my_list = input().split()

sum = 0
for item in my_list:
    sum += int(item)

# built-in function
"""
int
str
bool
float
sum
list
all
any
...
"""
# iterator     چیزی که میشه روی آن لوپ زد.
#
# map(method, iterator)

print(list(map(int, my_list)))  # [12, 13, 14]
print(my_list)  # ['12', '13', '14']
