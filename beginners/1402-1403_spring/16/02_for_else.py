# for else

my_list = ["mina", "jafar", "akbar", "soghra", "kubi"]

"""
Find 'asghar'
"""

# 1. membership operator
print("I found asghar" if "asghar" in my_list else "I didn't find asghar")

# 2. for and flag
has_asghar = False
for name in my_list:
    if name == "asghar":
        has_asghar = True
        break

print("I found asghar" if has_asghar else "I didn't find asghar")

# 3. for else
# if the loop doesn't break, It will execute else part.
# اگر حلقه شکسته نشود؛ قسمت
#  else
# اجرا میشود.
for name in my_list:
    if name == "asghar":
        print("I found asghar")
        break
else:
    print("I didn't find asghar")
