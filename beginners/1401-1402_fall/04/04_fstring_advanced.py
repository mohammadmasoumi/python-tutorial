# float 12.02020202
price = 12.00202202

print(f"price is: {price : 20.2f}")
# price is:                12.02
print(f"price is: {price:.400f}")
# 12.0202020199999992655648384243249893188476562500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
print(f"price is: {price:.04f}")
print(f"price is: {price:.4f}")
print(f"price is: {price : .4f}")
print("----------------------------------")

# space 
name = "Asghar"
name2 = "Mohammad"
name3 = "Hossein"

print(f"Name is: {name : >5}") # [][][][][a][s][g][h][a][r]
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
print(f"number is: {'آ':0100}")
print(f"number is: {'A':0100}")
print(f"number is: {1}")
print(f"number is: {1:02}")
print(f"number is: {2:03}") # [0][0][2]
print(f"number is: {2:3}") # [" "][" "][2]
print(f"number is: {10:020}")
print(f"number is: {10:02}")
print(f"number is: {100:02}") # [1][0][0]
print(f"number is: {100:04}") # [0][1][0][0]
print(f"number is: {1:03}")
print(f"number is: {1:013}")
print(f"number is: {1:13}")
# ValueError: Precision not allowed in integer format specifier
# print(f"number is: {1:0.13}")