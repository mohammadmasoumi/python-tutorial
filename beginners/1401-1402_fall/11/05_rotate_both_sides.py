# 2 r => 2 right rotate
# 2 l => 2 left rotate
my_list = [1, 2, 3, 4, 5]


# bool("Hello")
while "Hello":
    
    # Commands
    
    # Exit
    
    # [num][dir]
    # 2 r
    # 3 l

    # input().split()
    # items = ["Exit"]
    # n_rotate, direction = ["Exit"]  
    command = input()

    if command == "Exit":
        break

    # a, b = 12, 13
    # a, b = [12, 13]
    n_rotate, direction = command.split()
    n_rotate = int(n_rotate)

    if direction == "r":
        for _ in range( n_rotate % len(my_list)):
            my_list.insert(0, my_list.pop())
        print(my_list)

    elif direction == "l":
        for _ in range( n_rotate % len(my_list)):
            my_list.append(my_list.pop(0))
        print(my_list)
    else:
        print("Invalid direction")
