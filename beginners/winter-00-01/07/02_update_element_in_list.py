fruits = ["orange", "watermelon", "coconut"]

# append
# fruits.append("potato")
# TypeError: append() takes exactly one argument (2 given)
# fruits.append("potato", "tomato")
# fruits.append("potato tomato")
# fruits.append(["lemon", "onion"])

# iterable
# string is iterable
# fruits.extend("banana")
# fruits.extend(["banana", "cucumber"])

#  [ "banana" ,"orange", "watermelon", "coconut"]
# fruits.insert(0, "banana")
# [ "banana" , "orange", "watermelon", "coconut"]
# [ "banana" ,  "peach" ,"orange", "watermelon", "coconut"]
# fruits.insert(1, "peach")

# replace
# fruits.insert(0, "banana")
# fruits.remove("orange")
# fruits.pop(1)
print(fruits[0])
fruits[0] = "banana"
print(fruits[0])

print(fruits)

