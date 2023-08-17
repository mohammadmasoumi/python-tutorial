# While 

"""
CONDITION:  comparison operator
            logical operator

            variable > truthy falsy

while CONDITION {
    
}

"""


# comparison operator | logical operator
# a = 12
# b = 2
# while a > 2 and b > 0:
#     pass

# Variable > truthy falsy
# while True:
#     pass

# a = 1
# while a: # bool(a)
#     pass 

# 1.
cnt = 0
while cnt <= 10:
    print(f"Hello while cnt: {cnt}...")

    # break the wheel/wihle
    cnt += 1

# 2.
cnt = 0
while True:
    print(f"Hello while cnt: {cnt}...")

    if cnt == 10:
        break

    # print(f"Hello while cnt: {cnt}...")
 
    cnt += 1