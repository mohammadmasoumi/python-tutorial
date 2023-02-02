def handler(name, age):
    print(f"Handled, name: {name}, age: {age}")

def partial_function(f, name, age):
    def partial():
        return f(name, age)

    return partial


my_partial = partial_function(handler, "asghar", 22)
my_partial()
