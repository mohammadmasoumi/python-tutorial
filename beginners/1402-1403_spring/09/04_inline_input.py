"""
12
13
14

12 13 14
"12 13 14"
"""
n = input() # "12 13 14" => [12, 13, 14]

# print(n) 
# print(type(n))
my_list = []
num_so_far = ""

for char in n:
    # num_so_far: "", char: "1"
    # num_so_far: "1", char: "2"
    # num_so_far: "12", char: " "
    if char != " ":
        # num_so_far = num_so_far + char => "" + "1" => "1"
        # num_so_far: 1
        # num_so_far = num_so_far + char => "1" + "2" => "12"
        # num_so_far: 1
        # num_so_far: 12
        num_so_far += char 
    else:
        my_list.append(int(num_so_far)) # "12" => 12
        num_so_far = ""

# "14"
my_list.append(int(num_so_far))

print(my_list)
