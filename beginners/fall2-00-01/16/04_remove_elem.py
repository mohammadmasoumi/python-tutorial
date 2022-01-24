# remove or discard
set1 = {1, 2, 3, 4, 5}

print(set1)

# if item does no exist, it will raise exception
set1.remove(2)
# KeyError: 10

# set1.remove(10) # whether raise exception or not
# if item does no exist, it would not raise exception
set1.discard(3)
set1.discard(10) # whether raise exception or not

print(set1)
