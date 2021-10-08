# built-in function
# int()
# float()
# bool()
# str()
# list()
# id()
# for
# range(start_from, end_to, step)

# start_from: 0
# end_to: 10 (not_included)
# step: +1
a_range1 = range(10)
print(list(a_range1))

# start_from: 1
# end_to: 9
# step: +1
a_range2 = range(1, 10)
print(list(a_range2))

# start_from: 10
# end_to: 0
# step: -1
a_range3 = range(10, 0, -1)
print(list(a_range3))

fruits = ["apple", "orange", "banana"]
# len(fruits)
# fruits[0]
# fruits[1]
# fruits[2]]
i = 0
print(fruits[0])
print(fruits[i])

print("-----------------------------")
for item in fruits:
    print(item)

for idx in range(len(fruits)):
    print(idx, fruits[idx])

print("----------------------------~~")
