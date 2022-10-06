def hello(name):
    print("Hello")

def outer_function(score):
    def inner_function():
        hello("name")
    
    hello(print(inner_function(), inner_function()))

print(outer_function(10))