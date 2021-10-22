n = input()
counter = 0
jumps_count = 0
while counter < len(n) - 1:
    if counter + 2 < len(n) and n[counter + 2] != '1':
        jumps_count += 1
        counter += 2
    elif counter + 1 < len(n) and n[counter + 1] != '1':
        jumps_count += 1
        counter += 1

print(jumps_count)
