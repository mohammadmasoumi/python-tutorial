
my_list = ["orange", "lemon", "cucumber", "lemon", "banana", "orange"]

counter = 0

for item in my_list:

    if item == "orange":
        # print(f"item: {item}, counter: {counter}")
        my_list[counter] = "lemon"
    elif item == "lemon":
        my_list[counter] = "orange"

    counter += 1

print(my_list)