# input

# n: str
# n:"12"
# m = input("Please, enter a number: ")

# cast input to int permanently
# ValueError: invalid literal for int() with base 10: 'ali'

# n = int(input())

# n: "12"
# n: "ali"
# all the character must be digit

n = input()

if n.isdigit():
    n = int(n)
else:
    print("You must enter a digit.")

    