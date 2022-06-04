my_list=list(map(int,input().split()))
for i in range(len(my_list)):
    for j in range(len(my_list)-1-i):
        if my_list[j]<my_list[j+1]:
      #  if my_list[j]>my_list[j+1]:
            my_list[j],my_list[j+1]=my_list[j+1],my_list[j]
    
print(my_list)

