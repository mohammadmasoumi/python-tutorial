i = input("Please enter the inputs : (u / d)")

i = i.lower()

sea_level = 0

counter = 0

for item in i:
    if item == "u":
        sea_level += 1
    else:
        sea_level -= 1

    if sea_level == 0 and item == "u":
        counter += 1

print(counter)
