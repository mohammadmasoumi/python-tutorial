class CustomFileContextManger:

    def __init__(self, file_name, file_mode):
        # constructor
        print("run __init__")
        self.file_name = file_name
        self.file_mode = file_mode
        self.local_file = None

    def __enter__(self):
        print("run __enter__")
        self.local_file = open(self.file_name, self.file_mode)

        # self.connect = MongoClient('localhost', '27027')
        # return self.connect

        return self.local_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("run __exit__")
        self.local_file.close()

        # self.connection.close()


# [Common mistake]
# with CustomFileContextManger as file
# with CustomFileContextManger('file.txt', 'r') as mongo_connection:
with CustomFileContextManger('file.txt', 'r') as file:
    # file ===> opened_file

    # mongo_connection

    # enter to the context
    print("I am in the context.")
    print(file.readlines())

    # exit context

print("Bye")
