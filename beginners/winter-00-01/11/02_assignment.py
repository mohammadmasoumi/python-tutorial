
# index      0       1         2         3
my_list = ["ali", "mobin", "hassan", "hossein"]

# for and enumeration
# my_list = ["Hello_ali", "Hello_mobin", "Hello_hassan", "Hello_hossein"]

for idx, elem in enumerate(my_list):
    my_list[idx] = "Hello_" + elem
    # my_list[1] = "Hello_mobin"
    # my_list[2] = "Hello_hassan"
    # my_list[3] = "Hello_hossein"
    
print(my_list)