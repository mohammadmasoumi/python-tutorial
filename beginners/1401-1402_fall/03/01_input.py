# "12"
# Solution 1
# 12
# num1 = int(input("Enter a number: "))
# # 13
# num2 = int(input("Enter a number: "))

# Solution 2
# "12" "abc"
# input("Enter a number: ")
num1 = input("Enter a number: ")
num2 = input("Enter a number: ")

# num1 = int(num1)
# a = int(num1)

# Corner case
if num1.isdigit() and num2.isdigit():
    # Cast on the fly
    print(int(num1) + int(num2))

print(type(num1))