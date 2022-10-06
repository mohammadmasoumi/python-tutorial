my_list = [1, 2, 3, 4]
my_iterator = iter(my_list)

# for item in my_iterator:
#     print(item)
my_list.append(5)


while True:
    try:
        item = next(my_iterator)
        print(item)
        my_list.append(5)
        # code block 
        # for body

    except StopIteration:
        break
