# students

# 2D list
my_list = [[1, 2], [3, 4], [5, 6]]
# my_list = [
#    0  1
#   [1, 2], 0 
#   [3, 4], 1
#   [5, 6]  2
# ]

# first select row -> then select column

# my_list: list
# my_list[0]: list
# my_list[0][0]: int
print(my_list[0])
print(my_list[0][0])
print(my_list[2][0]) # 4? [5]?
# print(my_list[0][2]) # index out of range

# 3D list
my_list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

print(my_list[0]) # [[1, 2], [3, 4]]
print(my_list[0][0]) # [1, 2]
print(my_list[0][0][0]) # 1

# (my_list[0])[0][0]
# ([[1, 2], [3, 4]][0])[0]
# ([1, 2])[0]
# 1

# students

## inputs
# 3
# Ali 20 20 20
# Sina 10 10 10
# Mohammad 20 20 20
# (Sina)

## output
# print avg of sina

"""
1. [[name1, avg1], [name2, avg2], [name3, avg3]]
#     1 2           4 5
2. [names, ..., scores] -> [name1, name2, name3, avg1, avg2, avg3]
3. [name1, avg1, name2, avg2, name3, avg3]
4.  [name,, name2, name3]
    [avg1, avg2, avg3]

"""

print("-------------------------")
n = int(input()) # student count
students = []

for _ in range(n):
    # input(): "ALi 20 20 20" 
    # input().split(): ["ALi", "20", "20", "20"]
    items = input().split()
    # pop() -> remove last item
    # pop(index) -> remove indexed item
    
    # name: "Ali"
    # items: ["20", "20", "20"]
    name = items.pop(0)
    avg = sum(map(int, items)) / len(items)

    students.append([name, avg])


a, b = 10, 12
print(a, b)

a, b = [10, 12] # a: 10, b: 12
print(a, b)

idx, item = [0, 1] # idx: 0, item: 1
print(idx, item)

iname = input()
for name, avg in students:
    # item: [name, avg]
    # name, avg = item
    # name, avg = [name, avg]
    # name: item[0], avg: item[1]

    if iname == name:
        print(avg)
        break
else:
    print(f"{name} not found!") 

