fruits1 = ["apple", "orange" "watermelon", "cucumber"]

"""
a = 12
b = a
print(a)
print(b)
"""
fruits2 = fruits1

print(f"fruits1: {fruits1}")
print(f"fruits2: {fruits2}")

fruits1.append("peach")
fruits2.append("cherry")

print(f"fruits1: {fruits1}")
print(f"fruits2: {fruits2}")

# the same box
print(f"id fruits1: {id(fruits1)}")
print(f"id fruits2: {id(fruits2)}")

# I don't wanna add one item into fruit1 and fruit2
print("------------------------------------")
fruits3 = fruits1.copy()

fruits1.append("banana1")
fruits3.append("banana2")

print(f"fruits1: {fruits1}")
print(f"fruits3: {fruits3}")

# the same box
print(f"id fruits1: {id(fruits1)}")
print(f"id fruits3: {id(fruits3)}")
