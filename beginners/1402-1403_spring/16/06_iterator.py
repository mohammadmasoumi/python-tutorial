my_list = [1, 2, 3, 4, 5]

iterator = iter(my_list)

for item in iterator:
    # item = next(iterator)
    print(f"first: {item}")

"""
1
2
3
4
5
# StopIteration
"""

# new_iterator: iter(my_list)
for item in my_list:
    print(f"second: {item}")

"""
1
2
3
4
5
# StopIteration
"""

# iterator: exhausted
for item in iterator:
    # next(iterator) -> StopIteration
    print(f"third: {item}")

"""
exhausted iterator
"""