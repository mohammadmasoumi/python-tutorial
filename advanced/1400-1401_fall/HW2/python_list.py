my_list = []

for _ in range(int(input())):
    items = input().split()
    command = items[0]

    if command == 'append':
        my_list.append(int(items[1]))

    elif command == 'insert':
        my_list.insert(int(items[1]), int(items[2]))

    elif command == 'print':
        print(my_list)

    elif command == 'sort':
        my_list.sort()

    elif command == 'reverse':
        my_list.reverse()

    elif command == 'pop':
        my_list.pop()

    else:
        print("Wrong command!")
