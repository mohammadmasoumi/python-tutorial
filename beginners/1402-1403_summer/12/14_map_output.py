my_list = [1, 2, 3, 4, 5]
ouput = map(lambda x: x*2, my_list) # iterator

# generator
print(ouput) # <map object at 0x000001B32D52A920>
print(list(ouput)) # list, ['1', '2', '3', '4', '5']

# Disposable (یک بار مصرف) 
print("------------ 1 ------------")
for item in ouput:
    print(item)

print("------------ 2 ------------")
for item in ouput:
    print(item)

# ----
my_list = [1, 2, 3, 4, 5] # iterable
print("------------ 1 ------------")
for item in my_list: # iterator
    print(item)

print("------------ 2 ------------")
for item in my_list:
    print(item)

