# float 12.02020202
price = 12.02020202

print(f"price is: {price : 12.2f}")
print(f"price is: {price : .2f}")
print(f"price is: {price : .202f}")
# price is:  12.0202020199999992655648384243249893188476562500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

# space 
name = "Asghar"
name2 = "Mohammad"
name3 = "Hossein"
print(f"Name is: {name : >10}")
print(f"Name is: {name2 : >10}")
print(f"Name is: {name3 : >10}")
print("----------------------------------")
print(f"Name is: {name }, age: {12}")
print(f"Name is: {name2}, age: {32}")
print(f"Name is: {name3}, age: {22}")
print("----------------------------------")
print(f"Name is: {name : <20}, {' ':<10} age: {12: <10}, national_id:")
print(f"Name is: {name2 : <20}, {' ':<10} age: {32: <10}, national_id:")
print(f"Name is: {name3 : <20}, {' ':<10} age: {22: <10}, national_id:")
print("----------------------------------")
print(len("    Asghar"))

# number
print(f"number is: {1}")
print(f"number is: {1:02}")
print(f"number is: {2:02}")
print(f"number is: {10:020}")
print(f"number is: {10:02}")
print(f"number is: {100:02}")
print(f"number is: {100:04}")
print(f"number is: {1:03}")