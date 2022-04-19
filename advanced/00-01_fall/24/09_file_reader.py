class MyFileReader:

    def __init__(self, file_name):
        self._opened_file = open(f"{file_name}.txt")

    def __iter__(self):
        return self

    def __next__(self):
        # line = self._opened_file.readline().strip()
        line = self._opened_file.readline()

        # if line == "EOF":
        if line == "\n":
            print(f"line: {line}")
            self._opened_file.close()
            raise StopIteration

        return line


gen = MyFileReader('file')
for item in gen:
    print(item)

# with open("file.txt", "w") as file:
#     for i in range(10000):
#         file.write(f"Hello {i}\n")


# with open("file.txt", "r") as file:
#     for item in file.readlines():
#         # print(item.strip()) # "Hello1\n"
#         print(item, end="")
#         print(item)  # "Hello1\n\n"
