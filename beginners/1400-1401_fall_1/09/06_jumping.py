pathe = input()

jampe = 0
index = 0
while index < len(pathe) - 1:  # pathe : 0010010

    print(f"index: {index}, {len(pathe)}")

    if index + 2 < len(pathe) and pathe[index + 2] == "1":
        index += 2
        jampe += 1
    elif index + 1 < len(pathe) and pathe[index + 1] == "1":
        index += 1
        jampe += 1

print(jampe)
