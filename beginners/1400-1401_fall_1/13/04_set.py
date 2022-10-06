"""
add
update
remove
del
discard
---------------------
symmetric_difference
symmetric_difference_update
union
difference
difference_update
intersection
intersection_update
"""
# update

# append for list
# add for set
# update for dict
# tuple - immutable

a = {1, 2, 3, 4}

# del a
# print(a) # NameError: name 'a' is not defined
# add
a.add(6)
a.add(7)
a.add(10)

print(f"a: {a}")

# remove
a.remove(10)
# a.remove(20) # KeyError: 20
print(f"a: {a}")

# RuntimeError: Set changed size during iteration
# s1 = set(a)
s1 = set(a)
# {1, 2, 3, 4}
# {1, 2, 3, 4}
# for item in set(a):
for item in s1:
    if item != 1:
        a.remove(item)

print(a)

# del
# del a
# NameError: name 'a' is not defined
# print(f"a: {a}")
print("--------------------------------------------------")
a = {1, 2, 3, 4}

# iterable - list, tuple, set, range
a.update([1, 10, 20, 30])  # update set == extend list
a.update([100])  # TypeError: 'int' object is not iterable
# a: {1, 2, 3, 4, 100, 10, 20, 30}
# a.update(1) # TypeError: 'int' object is not iterable
# for item in [1, 10, 20, 30]:
#     a.add(item)

print(f"a: {a}")

# discard
a.discard(1000)  # if key does not exist, it won't raise exception.

# pop a random element -
c = a.pop()

#
print(f"a: {a}")

a10 = a.copy()

#
a.clear()
print(f"a: {a}")
print(f"a10: {a10}")
