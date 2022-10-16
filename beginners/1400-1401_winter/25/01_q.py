# "ali"
# "asghar"
# ord("l") ? ord("s") 
# "asghar" > "ali"

# a => 97
# A => 67

# "Ali"
# "ali"
# "Ali" ? "ali"

d = [
    {
        "name": "ali",
        "age": 22
    }, 
    {
        "name": "hassan",
        "age": 20
    },
    {
        "name": "asghar",
        "age": 19
    }
]

def sort_by_age(item):
    # {"name": "asghar", "age": 19}
    return item.get("age")  

def sort_by_name(item):
    # {"name": "asghar", "age": 19}
    return item.get("name")  


d.sort(key=sort_by_age)
print(d)

d.sort(key=sort_by_name)
print(d)
print("----------------------------------------")

f = [
    #  0     1
    ("ali", 22), 
    #  0        1
    ("hassan", 20),
    #  0        1 
    ("asghar", 19), 
]

def sort_by_age2(item):
    # ("ali", 22)
    return item[1]

def sort_by_name2(item):
    # 
    return item[0]

def sort_by_name3(item):
    # 
    return item[0][2]

# for item in f:
#     sort_value = sort_by_age2(item)

f.sort(key=sort_by_age2)
print(f)
f.sort(key=sort_by_name2)
print(f)
f.sort(key=sort_by_name3)
print(f)

# sorted(d.items(), key=)