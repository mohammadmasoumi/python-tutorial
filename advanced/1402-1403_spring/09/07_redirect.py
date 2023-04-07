import sys


class RedirectedStdout:
    def __init__(self, new_output):
        self.new_output = new_output

    def __enter__(self):
        self.saved_output = sys.stdout # terminal
        sys.stdout = self.new_output

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.saved_output


with open("output.txt", 'w') as file:
    with RedirectedStdout(file):
        print("Hello")

    print("Bye")
