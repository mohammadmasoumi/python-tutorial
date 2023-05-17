"""
rotate

1 2 3 4 5 [Base]
2 3 4 5 1 [n:1]
3 4 5 1 2 [n:2] *
4 5 1 2 3 [n:3]
5 1 2 3 4 [n:4]
1 2 3 4 5 [n:5]
2 3 4 5 1 [n:6]
3 4 5 1 2 [n:7] *
...
3 4 5 1 2 [n:12] *
=> mod

12 mod 5 => 2
"""
my_list = [1, 2, 3, 4, 5]
n = int(input())

# break down
n = n % len(my_list)

counter = 0

while counter < n:
    my_list.append(my_list.pop(0))
    counter += 1

print(my_list)
