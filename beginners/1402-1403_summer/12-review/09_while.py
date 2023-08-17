# while

"""
while CONDITION:
    -- start | while body


    -- end | while body

"""

count = 0
while count < 10:
    # do something

    count += 1


count = 0 
while True:
    # do something

    count += 1
    if count == 10:
        break


# for -> iterate over list

# while -> create step 
# inbalance steps
# execute a code manytimes

# 
counter = 0
while counter < 10:
    # execute code

    if counter % 2 == 0:
        counter += 2
    else: 
        counter += 1


# for item in [1, 2, 3, 4]:
#     print(item)