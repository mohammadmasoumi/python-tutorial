"""
list 
tuple
set
dict

iterable
sequence
iterator
"""
iterator = iter([1, 2, 3, 4])

for item in iterator:
    print(item)
    break

print("----------------")
print(next(iterator))
print("----------------")

# iterator.__next__()
# -> StopIteration
for item in iterator:
    print(item)