# my_list [20, 20, 20, 20] => Bravo
# my_list [20, 20, 18, 20] => Try more
# my_list [10, 10, 18, 10] => Call family

my_list  = [20, 20, 20, 20]

twenty_count = 0
for item in my_list:
    if item == 0:
        twenty_count += 1

if twenty_count == len(my_list):
    print("Bravo")
elif twenty_count == 0:
    print("Call ur family")
else:
    print("Try more")  
