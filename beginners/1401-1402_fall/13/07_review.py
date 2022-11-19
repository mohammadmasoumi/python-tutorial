# def adder(a, b):
#     # a, b = 12 , 13
#     # a: 12, b: 13
#     # a, b = 13, 14
#     return a + b

# # print(    25      )
# print(adder(12, 13))
# print(adder(13, 14))

def my_map(a, b):
    # a: lambda x: x // 2
    # b: [1, 2, 3 ,4]
    
    # def a(i):
    #       i: 1
    #       i: 2
    #     return i * 2

    new_list = []

    for item in b:
        # item: 1, new_list: [], 
        # item: 2, new_list: [2],                
        #                       2
        #                       4
        new_list.append(     a(item)    )
        # item: 1, new_list: [2],
        # item: 2, new_list: [2, 4],

    return new_list


print(my_map(lambda x: x // 2, [1, 2, 3 ,4]))