"""

---- input
3
Ali 19 19 20
Mohammad 20 20 20
Sina 10 10 10
Mohammad

---- output
20
"""
"""
my_list = [1, 2, 3, 4]

my_list.remove(3) # item

my_list.pop() # last item
my_list.pop(0) # index

item = my_list.pop()
"""

# n = int(input()) # str <- input()
# students: [["Ali", 20], ["Sina", 10], ["Mohammad", 20]]
students = [] 

for _ in range(int(input())):
    # "Ali 19 19 20"
    # "Ali 19 19 20".split()
    # items: ["Ali", "19", "20", "20"]
    # items: ["Mohammad", "20", "20", "20"]
    items = input().split()
    # name: "Ali"
    # items: ["19", "20", "20"]    
    name = items.pop(0)
    
    # sum
    s = 0
    for score in items:
        s += int(score)

    # avg
    avg = s / len(items)

    # pair key: value
    # name: "Ali"
    # avg: 20
    students.append([name, avg])

std_name = input()

# # students: [["Ali", 20], ["Sina", 10], ["Mohammad", 20]]
for name, avg in students: # name, avg = ["Ali", 20]
    if name == std_name:
        print(avg)
