# w => write
# r => read
# a => append
my_names = []

with open("name.txt", "r") as file:
    for item in file.readlines():
        print(item.strip())
        my_names.append(item.strip())

with open("name.txt", "a") as file:
    for item in my_names:
        file.write(item + "\n")

print(my_names)