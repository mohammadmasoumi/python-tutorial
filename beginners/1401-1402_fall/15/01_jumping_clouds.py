clouds = input()

#          ** * * **
# clouds: "110101111"
current_pos = 0
jump_count = 0

while current_pos < len(clouds):
    candidate_pos = current_pos + 2

    # clouds[candidate_pos] == "1" and candidate_pos < len(clouds)
    if candidate_pos < len(clouds) and clouds[candidate_pos] == "1":
        current_pos = candidate_pos
        jump_count += 1
    else:
        current_pos += 1
        jump_count += 1

print(jump_count - 1)
