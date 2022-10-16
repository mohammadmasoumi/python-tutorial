# Membership operator

# Iterable
my_list = [1, 2, 3, 4]

elem = 1

if elem in my_list:
    print(f"{elem} is a member of {my_list}")

elem = 10
if elem not in my_list:
    print(f"{elem} is not a member of {my_list}")


"""
is_exist = False
for (int i=0; i < len(my_list); i++) {
    if (my_list[i] == elem) {
        is_exist = True
        break
    }
}

if (is_exist == True) {

}
"""