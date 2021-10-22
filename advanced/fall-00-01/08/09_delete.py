set1 = {1, 2, 3, 4}

# delete - if does not exists, will not raise exception
set1.discard(5)
set1.discard(4)
print(set1)

# raise exception if does not exists
# KeyError: 5
try:
    set1.remove(5)
    print("Do not meet this line")
except KeyError as e:
    print(f"Error: {e}")
    print("I have gotten an error")
    # raise e
except Exception as e:
    pass
else:
    pass
finally:
    pass

set4 = {1, 2, 3, 4, 5}

# unordered
print(set4.pop())
set4.clear()
# set()
print(set4)

list1 = [1, 2, 3]
del list1[0]

# NameError: name 'set4' is not defined
del set4
print(set4)
