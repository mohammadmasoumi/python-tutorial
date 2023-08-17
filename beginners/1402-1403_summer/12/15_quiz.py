"""
Commands

append 2   | [2]
insert 0 1 | [1, 2]
extend 2 3 | [1, 2, 2, 3]
pop 0      | [2, 2, 3]
pop        | [2, 2]
remove 2   | [2]
print      | print list in terminal
exit       | no more input
"""
my_list = []

# del my_list[0]

while True:
    # args: ['append', '2']
    # args: ['insert', '0', '1']
    args = input().split()
    # command: append
    # args: ['2']
    command = args.pop(0)

    if command == 'exit':
        break
    
    elif command == 'append':
        my_list.append(int(args[0]))

    elif command == 'pop':
        if len(args) == 1:
            index = int(args[0])
            my_list.pop(index)
        else:
            my_list.pop()

    elif command == 'print':
        print(my_list)




