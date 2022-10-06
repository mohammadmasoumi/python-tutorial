# label: my_tuple1, my_tuple2
# |----------------|
# |                |
# |     12 , 13    |
# |                |
# |----------------|

my_tuple1 = (12, 13)
my_tuple2 = (12, 13)
my_tuple4 = (12, 14)

# چون ایتم های داخلیش یکسان هستند نیازی به تعریف جعبه جداگانه نیست
my_tuple5 = ("mohammad", "ali")  # the same
my_tuple6 = ("mohammad", "ali")  # the same

# بخاطر اینکه داخلش یک لیست تعریف کردیم که تغییر پذیر است
# پس دو تا جعبه تعریف میکند
my_tuple7 = ([1, 2], "a") # they are not the same
my_tuple8 = ([1, 2], "a") # they are not the same


# shortcut
# double ctrl + dow arrow
# esc
my_list1 = [12, 13]
my_list2 = [12, 13]
my_list3 = my_list2  # the same label

print(f"my_tuple1: {id(my_tuple1)}")
print(f"my_tuple2: {id(my_tuple2)}")
print(f"my_tuple4: {id(my_tuple4)}")
print(f"my_tuple5: {id(my_tuple5)}")
print(f"my_tuple6: {id(my_tuple6)}")
print(f"my_tuple7: {id(my_tuple7)}")
print(f"my_tuple8: {id(my_tuple8)}")

print("--------------------------")

print(f"my_list1: {id(my_list1)}")
print(f"my_list2: {id(my_list2)}")
print(f"my_list3: {id(my_list3)}")
