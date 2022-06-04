list1 = [21, 2, 3, 7, 18]

for i in range(len(list1)):
    min_index = 1
    min_item = 100
    
    for idx in range(i,len(list1)):
        if list1[idx] < min_item:
           min_item = list1[idx] 
           min_index = idx

    list1[i], list1[min_index] = list1[min_index], list1[i]

print(list1)
