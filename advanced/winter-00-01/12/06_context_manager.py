
with open("asghar.txt", "w") as f:
    # fob -> fobia
    f.write("Hello, welcome to the program.\n")


class CustomContextManager:

    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode
        self.opened_filed = ""

    def __enter__(self):
        self.opened_filed = open(self.file_name, self.file_mode)
        print("Enter to the context.")

        return self.opened_filed

    def __exit__(self, a, b, c):
        print("Exit from the context.")
        
        self.opened_filed.close()


with CustomContextManager("akbar.txt", "w") as file:
    print("I am in the context.")
    file.write("Hello ...... \n")

# with CustomContextManager(file_name, file_mode) as a:
#     pass