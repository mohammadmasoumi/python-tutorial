fruits = ["apple", "orange", "banana"]

print(fruits[0])
print(fruits[1])
print(fruits[2])

print("----------------")
for item in fruits:
    # body for loo[
    print(item)

    if item == "apple":
        continue  # skip
        # do not execute the rest of code

    print(item)
    # print(item)
    # do whatever you what

print("----------------")
# fruits = ["apple", "orange", "banana"]
for item in fruits:
    # body for loo[
    print(item)

    if item == "apple":
        break  # break
        # break the for loop

    print(item)
    # print(item)
    # do whatever you what
