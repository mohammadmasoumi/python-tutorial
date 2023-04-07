
"""
WITH CONTEXT_MANAGER


try:

except:

finally:

"""

# with open("file.txt", "w") as file:
#     # enter => open
#     file.write("Hello")
#     # exit => close

# print("hello")


class FileContextManager:

    def __init__(self, file_name,file_mode):
        self.file_name = file_name
        self.file_mode = file_mode
        self.f = None

    def __enter__(self):
        print("Entered")
        self.f = open(self.file_name, self.file_mode)
        return self.f

    # def __exit__(self, *args)):
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exited")
        self.f.close()


with FileContextManager("newfile.txt", "w") as file:
    file.write("NewContextManager")