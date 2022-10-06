n = input()

current_pos = 0
jump_count = 0

while True:
    next_cloud_pos_candidate = current_pos + 2

    if next_cloud_pos_candidate < len(n) and n[next_cloud_pos_candidate] == "1":
        current_pos += 2
        jump_count += 1
    else:
        current_pos += 1
        jump_count += 1

    if current_pos == len(n) - 1:
        print(jump_count)
        break
        