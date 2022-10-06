def my_function():
    
    def wrapper():
        print("Hello")

    return wrapper


# new: wrapper
new = my_function()

# Outputs "Hello"
new()