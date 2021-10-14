my_list = [1, 2, 3, 4, 5, 5]

# declare in key words


# first solution
have_met_so_far = []

for item in my_list:
    if item not in have_met_so_far:
        have_met_so_far.append(item)
