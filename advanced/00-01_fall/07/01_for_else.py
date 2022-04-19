my_list = [1, 2, 3, 4]

num = 2

# for else
for item in my_list:
    if item == num:
        break
        # continue
else:
    print(f"I could not find {num}")

# --------------------------------------------
# alternative

# flag
is_found = False

for item in my_list:
    if item == num:
        is_found = True
        break

if not is_found:
    print(f"I could not find {num}")
