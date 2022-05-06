my_list = ["mobin", "mahdi", "asghar"]

"""
if
else

Ali -> `I find Ali`
not Ali -> `I didn't find Ali`
"""
# I've seen ali or not
flag = False

for name in my_list:
    if name == "ali":
        print("I find Ali")
        flag = True
        break
    
if not flag:
    print("I didn't find Ali")

