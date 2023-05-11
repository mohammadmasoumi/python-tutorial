"""

Rotate

1 2 3 4 5

5 1 2 3 4 [1]
4 5 1 2 3 [2]
3 4 5 1 2 [3]
2 3 4 5 1 [4]
1 2 3 4 5 [5]
5 1 2 3 4 [6]

19876 % len(list) = 1

Shift

1 2 3 4 5
  1 2 3 4
    1 2 3

"""


my_list = [1, 2, 3, 4, 5]
n = int(input())

n = n % len(my_list)

counter = 0

while counter < n:
    item = my_list.pop(-1)
    my_list.insert(0, item)
    counter += 1

print(my_list)