


first_string = input()
second_string = input()


# [BE CAREFUL] NOT  first_string > second_string - this compares strings, not their length
if len(first_string) > len(second_string):
    bozorgtar, kochektar = first_string, second_string
else:
    kochektar, bozorgtar = first_string, second_string


diff = 0


for index in range(len(bozorgtar)):

    if index < len(kochektar):
        if bozorgtar[index] != kochektar[index]:
            diff += 1
    else:
        diff += 1

print(diff)