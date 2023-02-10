# Membership operator
my_list = [1, 2, 3, 4]

"""
is_exists = False
for (int i=0; i<4; i++){
    if (my_list[i] == item) {
        is_exists = True
        break
    }
}

# MEMBERSHIP OPERATOR
 - IN
 - NOT IN

"""

if 2 in my_list:
    print("I found 2")

if 5 in my_list:
    print("I found 5")

if 5 not in my_list:
    print("I didn't found 5")