# Methods on list

my_list = ["apple", "watermelon", "banana", "cucumber", "apricot", "lemon"]

# append
my_list.append("orange")
my_list.append(["orange", "apple"])
print(my_list)
print("-----------")

# insert
#  [   "cherry"     ,"apple", "watermelon", "banana", "cucumber", "apricot", "lemon"]
my_list.insert(0, "cherry")
# [   "cherry"     ,"apple", "watermelon", "banana", "cucumber", "apricot",   "strawberry"    ,"lemon"]
my_list.insert(6, "strawberry")
# [   "cherry"     ,"apple", "watermelon", "banana", "cucumber", "apricot",   "strawberry"    ,"lemon", "grape"]
my_list.insert(10000, "grape")

print(my_list)

# extend
my_list.extend("orange")
my_list.extend(["orange"])
my_list.extend(["orange", "apple"])

print(my_list)
# my_list.extend(["orange", "apple"])

