# 1
# scores = [10, 20, 20, 18]
# # scores = [20, 20, 20, 20]
# # scores = [10, 10, 10, 10]

# at_least_one_item = False
# all_items = True

# for score in scores:
#     if score == 20:
#         at_least_one_item = True
#     else:
#         all_items = False

# if all_items:
#     print("Bravo")
# elif at_least_one_item:
#     print("Try more")
# else:
#     print("Awful")

# 2
# scores = [10, 20, 20, 18]
# scores = [20, 20, 20, 20]
# scores = [10, 10, 10, 10]

# count = 0

# for score in scores:
#     if score == 20:
#         count += 1

# if count == len(scores):
#     print("Bravo")
# elif count > 0:
#     print("Try more")
# else:
#     print("Awful")

# 3

# datatype
# truthy, falsey 

# falsey
# "", [], 0, 0.0, False

# all - if all items are truthy => True

# any - at least one item is truthy => True

scores = [10, 20, 20, 18]
print(all(scores))
print(any(scores))
print("------------------")

scores = [10, 20, 20, 0]
print(all(scores))
print(any(scores))
print("------------------")

scores = [20, 18, 18]

index = 0
for score in scores:
    if score == 20:
        scores[index] = 1
    else:
        scores[index] = 0
    
    index += 1

# scores = [1, 0, 0]

"""
def all(iterable: Iterable[object], /) -> bool
Return True if bool(x) is True for all values x in the iterable.

If the iterable is empty, return True.
"""
print(all(scores))

"""
scores = [[], []]
def all(iterable: Iterable[object], /) -> bool
Return True if bool(x) is True for all values x in the iterable.

If the iterable is empty, return True.
"""
print(any(scores))


if all(scores):
    print("Bravo")
elif any(scores):
    print("Try more")
else:
    print("Awful")