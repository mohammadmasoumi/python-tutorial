# 
my_list = ['20', '20', '19']

# my_list = [20, 20, 19] ?

for idx, item in enumerate(my_list):
    # print(idx, item)
    my_list[idx] = int(item)


for item in my_list:
    print(item , type(item))

# print(my_list)