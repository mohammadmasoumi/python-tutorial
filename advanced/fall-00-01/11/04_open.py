with open('C:\\Users\\mft\\Desktop\\Text.txt', "w") as write_file:
    with open("02_validate_class.py", "r") as read_file:
        for line in read_file.readlines():
            write_file.write(line)
