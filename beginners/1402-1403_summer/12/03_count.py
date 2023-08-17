# Count

my_list =  ["hello", "bye", "bye", 1, 2, "12", 12.2, "12", 2]
result = []

for item in my_list:
    # search item in result
    # for else
    # if loop does not break -> execute else
    for elem in result:
        #          0     1
        # elem: [item, count]
        # elem: ["bye", 1], item: "hello"
        if item == elem[0]:
            # exist -> ++count
            elem[1] += 1 
            break
    else:
        result.append([item, 1])

print(result)