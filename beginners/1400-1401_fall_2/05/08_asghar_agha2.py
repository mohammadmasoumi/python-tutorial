#            0          1        2           3           4             5
fruits = ["orange", "banana", "apricot", "cucumber", "watermelon", "orange"]
# fruits = ["orange", "banana",  "peach"        , "apricot", "cucumber", "watermelon", "orange"]
# fruits = ["orange", "banana",   "peach"       ,   "apricot", "cucumber", "watermelon", "orange"]
# fruits = [ "banana", "apricot", "cucumber", "watermelon", "orange"]

"""
if variable type is list
variable_name(.)(method_name)
"""

# 1
# Number of occurrences of value.
print(fruits.count('orange'))

# 4
# Insert object before index.
#          index   item
fruits.insert(2, "peach")
print(fruits)
# print(fruits[2])

# 5
# Remove first occurrence of value.
# fruits.count("orange")
# fruits.remove("orange")
# fruits.remove("orange")
# fruits.remove("watermelon")

# در این حالت شما خروجی تابع remove را میخواهید چاپ کنید.
# print(fruits.remove("watermelon"))

fruits.remove("watermelon")
# print(int("12"))
print(fruits)

"""
fog
f(g(x))  / c = g(x)
f(c)
"""

# 6
fruits.append("cherry")
print(fruits)

# 7
# update - remove + insert
fruits[4] = "pineapple"
print(fruits)
