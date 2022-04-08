a = [12, 13]

print(id(a))
print(id(a[0]))
print(id(a[1]))
print(id(a[1]) - id(a[0]))
print("-----------------------")

# append 
a.append(14) # a = [12, 13, 14]
print(id(a[1]) - id(a[0]))
print(id(a[2]) - id(a[1]))
print("-----------------------")

# insert 
# a = [12, 15, 13, 14]
a.insert(1, 15)
print(id(a[1]) - id(a[0]))
print(id(a[2]) - id(a[1]))
print(id(a[3]) - id(a[2]))