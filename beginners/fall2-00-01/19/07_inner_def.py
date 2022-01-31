def hello():
    print("Hello")

def outer_function(score):
    def inner_function():
        hello()

print(outer_function(10))