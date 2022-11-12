# # for else

# # 1.
# for item in []:
#     print(item)
# else:
#     print("Bye")

# # 2.
# for item in ["hello", "world"]:
#     if item == "hello":
#         break
# else:
#     print("I found Hello")


names = ["ali", "asghar", "akbar", "hassan"]

# 1. Membership operator
# if "asghar" in names:
#     print("I found asghar")
# else:
#     print("I didn't find asghar")


"""
for name in names:
    if name.startswith("b"):
        print("It starts with b")
    else:
        print("No word starts with b")


flag = False
for name in names:
    if name.startswith("b"):
        flag = True
        break

if flag:
    print("It starts with b")
else:
    print("No word starts with b")
"""
# 1.
for name in names:
    if name.startswith("b"):
        print("It starts with b")
        break
else:
    # if loop hasn't broken yet
    print("No word starts with b")

# 2.
for name in names:
    if name.startswith("b"):
        print("It starts with b")
        break
    else:
        # if loop hasn't broken yet
        print("No word starts with b")