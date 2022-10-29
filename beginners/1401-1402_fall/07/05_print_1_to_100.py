# 1. 
counter  = 1

while counter <= 100:
    # counter: 99
    # counter: 100
    # counter: 101
    print(counter)
    counter += 1

# 2. 
items  = [0] * 100
counter = 1

for item in items:
    print(counter)
    counter += 1
    # print(f"print({counter})")

# 3. 
items = [1]

# [1]
# [1, 2]
# [1, 2, 3]

for item in items:
    # 99
    # [1, 2, 3, .... 99]
    # [1, 2, 3, .... 99, 100]
    print(item)

    if item == 100:
        break

    items.append(item+1)
    

print(items)

# 4.
counter  = 1

while True:
    # counter: 99
    # counter: 100
    # counter: 101
    print(counter)

    if counter == 100:
        break

    counter += 1

# 5. 
"""
class range(start: int, stop: int, step: int=...)
range(stop) -> range object
range(start, stop[, step]) -> range object
"""
# default start: 0
# default step: 1
#                 start end
for number in range(1, 101):
    print(number)

#                    end
# print 0 to 100
for number in range(101):
    print(number)

# range(1, 101)
items = range(1, 101)
print(items, type(items))

items = list(range(1, 101))
print(items)


items = list(range(101))
print(items)

print("------------------------")
# print 0 to 100
for number in range(101):
    print(number)

print("*******************")
#                   start end
for number in range(101, 2):
    print(number)

print("##############################")
#                    100
#                    -1
# [100, 99, ...., 1, 0 ]
items = [range(100, -1, -1)]
print(items[100: -1: -1])

for number in range(100, -1, -1):
    print(number)

print("##############################")
# for number in range(100, , -1):
#     print(number)

#     start end step
# print(range(100, , -1))
print(list(range(100, 2, -1)))
print(list(range(100, 2, -2)))
print("##############################")


my_list = [1, 2, 3, 4]
# range(len(my_list))
# [0, 1, 2, 3]
for index in range(len(my_list)):
    print(index, my_list[index])