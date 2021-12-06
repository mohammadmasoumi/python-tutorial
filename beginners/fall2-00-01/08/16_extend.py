fruits1 = ["apple", "orange", "watermelon", "cucumber"]
fruits2 = ["cherry", "peach"]

fruits1.append("banana")
#                 iterable
# fruits1.extend("banana1")
# fruits1.extend(["banana1"], ["banana2"])

fruits1.extend(["banana1", "banana2", "banana3"])
fruits1.extend(fruits2)

print(fruits1)
print(fruits2)
