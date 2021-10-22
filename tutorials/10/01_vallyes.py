n = int(input())
trip = input()

sea_level = 0
valleys = 0
for step in trip:
    if step == 'U':
        sea_level += 1
    else:
        sea_level -= 1

    if sea_level == 0 and step == 'U':
        valleys +=1

print(valleys)

